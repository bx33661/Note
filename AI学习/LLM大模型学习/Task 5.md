# Task 5 系统评估和优化

---



## 评估优化流程

![image-20240628204055431](C:/Users/lenovo/AppData/Roaming/Typora/typora-user-images/image-20240628204055431.png)

> 在具体的大模型应用开发中，我们通过寻找并优化Bad Cases来提高系统性能。我们将每个Bad Case加入到验证集中，并在每次优化后重新验证所有案例，以确保系统不会在原有Good Case上失去能力或表现降级。当验证集较小时，我们可以通过人工评估系统输出的优劣。但随着验证集不断扩张，我们需要采用自动评估的方法来评估系统性能。在本文中，我们将介绍人工评估的思路，深入探讨大模型自动评估的方法，并在本系统上进行实际验证，全面评估系统表现，为优化迭代做准备。接下来，我们将加载向量数据库和检索链。

### 人工评测

- 量化评估

## 基于gradio

> 在上一个任务Task 4时候我们跟着DW的教程基于Streamlit搭建并部署了一个应用，如下图所示：
>
> ![image-20240626222019668.png](https://s2.loli.net/2024/06/26/jheZAKFsUBvW1Ig.png)
>
> 随着深入地学习，又遇见了一个新的广泛应用的框架，我尝试一下

具体实现代码如下：

- 采用DW封装的--zhipuai_llm.py
- 采用DW封装的--zhipuai_embedding.py

```python
import gradio as gr
from zhipuai_llm import ZhipuAILLM
from zhipuai import ZhipuAI
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())    
import os

zhipuai_api_key = os.environ['ZHIPUAI_API_KEY']

# 初始化 ZhipuAI 客户端
client = ZhipuAI(api_key=zhipuai_api_key)

# 定义模型名称列表
model_options = ["glm-4-0520", "glm-3-1105", "glm-2-0301"]

# 生成响应的函数
def generate_response(input_text, model_name, chat_history):
    llm = ZhipuAILLM(model=model_name, temperature=0.3, api_key=zhipuai_api_key)
    response = llm(input_text)
    chat_history.append(("User", input_text))
    chat_history.append(("AI", response))
    return chat_history, chat_history

# 生成AI绘画的函数
def generate_art(prompt):
    response = client.images.generations(
        model="cogview-3",
        prompt=prompt,
    )
    image_url = response.data[0].url
    return image_url

# 定义介绍信息
def introduction():
    return "这是一个基于 Gradio 搭建的对话和绘画应用，使用的是智谱AI的大模型。请选择模型并输入文本进行对话或生成绘画。"

# 搭建 Gradio 界面
with gr.Blocks(css="""
    body {font-family: 'Arial', sans-serif; background-color: #f4f4f9;}
    h1 {color: #333; text-align: center; margin-top: 20px;}
    .container {max-width: 800px; margin: auto; padding: 20px;}
    .gr-button {background-color: #4CAF50; color: white; border: none; padding: 10px 20px; cursor: pointer;}
    .gr-button:hover {background-color: #45a049;}
    .gr-dropdown, .gr-textbox {width: 100%;}
    .gr-chatbot {max-height: 400px; overflow-y: auto; background-color: white; padding: 20px; border-radius: 10px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);}
""") as demo:
    gr.Markdown("# 大模型对话和绘画应用")
    gr.Markdown(introduction())

    with gr.Tabs():
        with gr.TabItem("对话"):
            with gr.Row():
                model_choice = gr.Dropdown(choices=model_options, value=model_options[0], label="选择模型")
            
            chatbot = gr.Chatbot(label="对话", elem_id="chatbot")
            input_text = gr.Textbox(label="输入文本", placeholder="请输入你的问题...", lines=1)
            submit_button = gr.Button("提交")

            chat_history_state = gr.State([])  # 初始化对话历史

            # 设置按钮点击事件
            submit_button.click(generate_response, inputs=[input_text, model_choice, chat_history_state], outputs=[chat_history_state, chatbot])

        with gr.TabItem("AI绘画"):
            art_prompt = gr.Textbox(label="绘画提示词", placeholder="请输入绘画提示词...", lines=1)
            generate_button = gr.Button("生成绘画")
            art_output = gr.Image(label="生成的绘画")

            # 设置生成绘画按钮点击事件
            generate_button.click(generate_art, inputs=art_prompt, outputs=art_output)

# 启动 Gradio 应用
demo.launch(share=True)
```



![image-20240628201229240](https://s2.loli.net/2024/06/28/o7kZz4tyYqpQI2A.png)

![image-20240628201930177](https://s2.loli.net/2024/06/28/leoDTx6nCLJgzSV.png)

```python
def generate_response(input_text, model_name, chat_history):
    llm = ZhipuAILLM(model=model_name, temperature=0.3, api_key=zhipuai_api_key)
    response = llm(input_text)
    chat_history.append(("User", input_text))
    chat_history.append(("AI", response))
    return chat_history, chat_history

# 生成AI绘画的函数
def generate_art(prompt):
    response = client.images.generations(
        model="cogview-3",
        prompt=prompt,
    )
    image_url = response.data[0].url
    return image_url
```

两个函数`generate_response` 和 `generate_art`接入**智谱**的api进行内容生成

