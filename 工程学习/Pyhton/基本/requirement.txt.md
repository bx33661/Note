### requirement.txt

> 让claude帮我整理的

`requirements.txt` 是一个在 Python 项目中常用的文件，它列出了项目所依赖的所有 Python 包（库）及其版本。这个文件的主要用途和重要性如下：

1. 依赖管理：
   - 列出项目需要的所有外部库。
   - 指定每个库的版本，确保项目在不同环境中的一致性。
2. 环境复制：
   - 方便在不同机器上重建相同的开发环境。
   - 对于团队协作和部署非常有用。
3. 安装简化：
   - 使用 `pip install -r requirements.txt` 命令可以一次性安装所有依赖。
4. 版本控制：
   - 通常与版本控制系统（如 Git）一起使用，跟踪项目依赖的变化。
5. 文件格式：
   - 通常每行一个包，格式为 `package_name==version`。
   - 例如：`Flask==2.0.1`
6. 版本指定：
   - 可以指定确切版本、最小版本或版本范围。
   - 例如：`requests>=2.25.1,<3.0.0`
7. 生成方法：
   - 可以手动创建和编辑。
   - 也可以使用 `pip freeze > requirements.txt` 自动生成。
8. 最佳实践：
   - 定期更新以包含最新的安全补丁。
   - 在虚拟环境中管理依赖，避免全局安装带来的冲突。

----

#### 生成方法

- 手写

- 利用自动这个，但是环境内所有的包都会被包含在内

```
pip freeze > requirements.txt
```

- 使用 pipreqs

```python
pip install pipreqs
pipreqs .
#更多的看官网把
```

