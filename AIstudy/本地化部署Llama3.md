*最近开源的llama模型非常火，BX同学在这里向大家演示一下，如何本地部署。
本文章谨代表BX个人思考*
![](https://img-blog.csdnimg.cn/img_convert/d5579fdc214175ec5def64be541fe90c.png#id=grVJ0&originHeight=1347&originWidth=2560&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)
Meta公司发布的新一代大语言模型，

> 本期介绍如何在本地，在自己电脑上利用CPU/GPU部署运行，


---

## 介绍：![](https://img-blog.csdnimg.cn/img_convert/e72b8308f37ee3ae6948e5df180e3c0f.png#id=bDwKL&originHeight=360&originWidth=905&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)

## 第一步:

用Ollama
![](https://img-blog.csdnimg.cn/img_convert/507714cc2df9d58a9960bab72c077888.png#id=VHDME&originHeight=97&originWidth=79&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)
下载ollama：
[https://ollama.com/](https://ollama.com/)

## 第二步：

下载Docker desk：[https://www.docker.com/get-started/](https://www.docker.com/get-started/)
![](https://img-blog.csdnimg.cn/img_convert/cb051fcc3754963e21c8233ad6c8b7e1.png#id=aKG8s&originHeight=1347&originWidth=2560&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)
根据提示操作 按部就班 的下载

检查：
![](https://img-blog.csdnimg.cn/img_convert/cfbb8bac824eba12412c69929510f43f.png#id=vC13W&originHeight=1194&originWidth=1730&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)

## 第三步：

下载 **open-webui**框架

- GitHub：[https://github.com/open-webui/open-webui](https://github.com/open-webui/open-webui)
- 在cmd/powershell中

```powershell
docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main
```

- ![](https://img-blog.csdnimg.cn/img_convert/541f12623767836644ea9d0303617318.png#id=jvT8q&originHeight=745&originWidth=1730&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)

这样就安装完成了

## 第四步：

![](https://img-blog.csdnimg.cn/img_convert/1c2566982a75864b582d127fef60ad05.png#id=SVSYH&originHeight=1080&originWidth=1905&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)
在docker中运行这个项目
![](https://img-blog.csdnimg.cn/img_convert/adcb260d9f4454b2040d65a5ca7f6ce7.png#id=PRYgy&originHeight=1080&originWidth=1905&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)
然后进入：

> [http://localhost:3000/](http://localhost:3000/)


## 第五步：

注册登录后进入界面
![](https://img-blog.csdnimg.cn/img_convert/35b546eae9fa0e368099fc434027d5ef.png#id=RW4Xl&originHeight=1347&originWidth=2560&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)
然后进入设置去下载模型
![](https://img-blog.csdnimg.cn/img_convert/c3dd10ec93b534faf88af7a08ffb9aa4.png#id=aLPZB&originHeight=1347&originWidth=2560&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)
进入到模型选择界面
![](https://img-blog.csdnimg.cn/img_convert/fcdca4ef130fa5f756e32c2697874553.png#id=dgie1&originHeight=1347&originWidth=2560&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)
有一个70B和8B和两种情况，根据自己的情况去下载
![](https://img-blog.csdnimg.cn/img_convert/c3677263a2f41e9bbcd592fa31bccbf4.png#id=H19bc&originHeight=1347&originWidth=2560&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)
![](https://img-blog.csdnimg.cn/img_convert/b665a73a538bfc367130b87e182e18b3.png#id=NgGu4&originHeight=1347&originWidth=2560&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)
把下载指令填入下载框，等待下载就行了

## 最后一步：

![](https://img-blog.csdnimg.cn/img_convert/adeff994110e45786c6b1d4c69ecc8c1.png#id=FwD17&originHeight=1347&originWidth=2560&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)
选择模型就可以开始对话了

![](https://img-blog.csdnimg.cn/img_convert/5d9e15b7a153a9df8db1ad23bdd01482.png#id=P98cS&originHeight=1347&originWidth=2560&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)
效果还是很不错！

---

感谢大家观看，让我们一起进步
