GitHub 提供了强大的搜索功能，允许你根据各种条件查找仓库、代码、用户、议题（Issues）等。掌握这些搜索语法可以极大地提高你的工作效率。以下是对 GitHub 搜索语法的全面讲解：

**基本搜索**

在 GitHub 网站的搜索栏中输入关键词即可进行基本搜索。GitHub 会在仓库名称、描述、代码以及其他内容中查找匹配项。

**使用限定符**

限定符可以帮助你缩小搜索范围，更精确地找到你需要的内容。以下是一些常用的限定符：

- **`repo:`**: 搜索特定的仓库。例如：`repo:facebook/react` 搜索 Facebook 的 React 仓库。
- **`user:`**: 搜索特定用户的仓库。例如：`user:google` 搜索 Google 用户的所有公共仓库。
- **`org:`**: 搜索特定组织的仓库。例如：`org:apache` 搜索 Apache 组织的所有仓库。
- **`language:`**: 搜索特定编程语言的仓库。例如：`language:python` 搜索使用 Python 编写的仓库。
- **`topic:`**: 搜索具有特定主题的仓库。例如：`topic:machine-learning` 搜索与机器学习相关的仓库。
- **`stars:`**: 搜索拥有特定数量星标的仓库。例如：`stars:>1000` 搜索星标数超过 1000 的仓库。
- **`forks:`**: 搜索拥有特定数量 Fork 的仓库。例如：`forks:<100` 搜索 Fork 数少于 100 的仓库。
- **`created:`**: 搜索在特定日期或日期之后创建的仓库。例如：`created:>2023-10-26` 搜索 2023 年 10 月 26 日之后创建的仓库。
- **`pushed:`**: 搜索最近有推送的仓库。例如：`pushed:<2023-10-26` 搜索在 2023 年 10 月 26 日之前推送的仓库。
- **`size:`**: 搜索特定大小的仓库。例如：`size:<1000` 搜索小于 1MB 的仓库 (单位为 KB)。
- **`filename:`**: 搜索包含特定名称的文件。例如：`filename:LICENSE` 搜索包含名为 LICENSE 的文件的仓库。
- **`path:`**: 搜索特定路径下的文件。例如：`path:docs` 搜索 `docs` 目录下的文件。
- **`extension:`**: 搜索具有特定文件扩展名的文件。例如：`extension:txt` 搜索扩展名为 txt 的文件。
- **`in:`**: 指定在哪个字段中搜索。例如：`in:name react` 只在仓库名称中搜索 react。`in:description react` 只在仓库描述中搜索 react。

**使用运算符**

- **`AND`**: 同时满足多个条件。例如：`language:python stars:>100` 搜索使用 Python 编写且星标数超过 100 的仓库。默认情况下，多个关键词之间是 AND 关系，所以 `python machine-learning` 等同于 `python AND machine-learning`。
- **`OR`**: 满足任意一个条件。例如：`language:python OR language:javascript` 搜索使用 Python 或 JavaScript 编写的仓库。
- **`NOT` 或 `-`**: 排除某个条件。例如：`language:python NOT topic:machine-learning` 或 `language:python -topic:machine-learning` 搜索使用 Python 编写但与机器学习无关的仓库。
- **引号 `""`**: 搜索完全匹配的短语。例如：`"hello world"` 搜索包含 “hello world” 这个完整短语的内容。

**数值比较**

- **`>`**: 大于。例如：`stars:>1000`
- **`>=`**: 大于等于。例如：`stars:>=1000`
- **`<`**: 小于。例如：`stars:<1000`
- **`<=`**: 小于等于。例如：`stars:<=1000`
- **`..`**: 范围。例如：`stars:100..500` 搜索星标数在 100 到 500 之间的仓库。

**日期搜索**

日期可以使用 `YYYY-MM-DD` 格式，也可以使用相对时间。

- `created:2023-10-26`
- `created:>2023-10-20`
- `created:<2023-11-01`

**组合使用**

可以将多个限定符和运算符组合起来，创建非常复杂的搜索查询。

例如：`repo:facebook/react language:javascript stars:>10000 in:readme "redux"` 搜索 Facebook 的 React 仓库中，使用 JavaScript 编写，星标数超过 10000，并且 README 文件中包含 "redux" 的内容。

**一些实用技巧**

- 使用高级搜索页面：GitHub 提供了一个高级搜索页面，可以帮助你更方便地构建复杂的搜索查询。（在 GitHub 搜索框输入后，点击 “Advanced Search” 进入）
- 善用浏览器的搜索功能：在 GitHub 页面上，可以使用浏览器自带的搜索功能（通常是 Ctrl+F 或 Cmd+F），在当前页面查找内容