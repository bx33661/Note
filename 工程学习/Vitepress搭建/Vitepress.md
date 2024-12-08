<meta name="referrer" content="no-referrer">
## Vitepress

[[TOC]]

> @Author:bx33661
>
> @content:主要是记录基于Vitepress快速搭建文档站的过程
>
> @Web：http://doc.bx33661.com

官方网站：https://vitepress.dev/

VitePress 是一个[静态站点生成器](https://en.wikipedia.org/wiki/Static_site_generator) (SSG)，专为构建快速、以内容为中心的站点而设计。简而言之，VitePress 获取用 Markdown 编写的内容，对其应用主题，并生成可以轻松部署到任何地方的静态 HTML 页面。

![image-20241202233346497](https://gitee.com/bx33661/image/raw/master/path/image-20241202233346497.png)

---

一般项目结构

```bash
.
├─ docs
│  ├─ .vitepress
│  │  └─ config.js
│  ├─ api-examples.md
│  ├─ markdown-examples.md
│  └─ index.md
└─ package.json
```

VitePress 使用 **基于文件的路由**：每个 `.md` 文件将在相同的路径被编译成为 `.html` 文件。例如，`index.md` 将会被编译成 `index.html`，可以在生成的 VitePress 站点的根路径 `/` 进行访问

### 展示效果

1. BX-Doc

   ![image-20241202234721618](https://gitee.com/bx33661/image/raw/master/path/image-20241202234721618.png)

2. YY-Blog

![image-20241202234655389](https://gitee.com/bx33661/image/raw/master/path/image-20241202234655389.png)

### 初始化

首先要有Nodejs环境

- 可以自己从空白开始

```(空)
npm add -D vitepress
npx vitepress init
```

设置默认选项就行

![image-20241202234125827](https://gitee.com/bx33661/image/raw/master/path/image-20241202234125827.png)

```(空)
npm run docs:dev
```

![image-20241202234340386](https://gitee.com/bx33661/image/raw/master/path/image-20241202234340386.png)

我们访问5173就可以看到一个基本站点

![image-20241202234425790](https://gitee.com/bx33661/image/raw/master/path/image-20241202234425790.png)

- 或者使用别人已经配置好的仓库

> 这里推荐几个：
> https://github.com/Charles7c/charles7c.github.io?tab=readme-ov-file
>
> https://github.com/shoppingzh/vitepress-template/

就是各种插件和基本配置已经完成了，你只需要稍微修改就行，就是不需要自己造轮子了



### 侧边栏操作

1. 可以采用自动生成侧边栏的插件

https://vitepress-sidebar.cdget.com/zhHans/

![image-20241205182759989](https://gitee.com/bx33661/image/raw/master/path/image-20241205182759989.png)

2. 官方文档自己配置

在`themeconfig`中,根据路由自动设置

下面是一个多级侧边栏示例：

```yaml
sidebar: {
    // 当用户位于 'docc' 目录时，会显示此侧边栏
    '/docc/': [
      {
        text: 'BTool文档',
        items: [
          { text: '介绍', link: '/docc/index.md' },
          { text: 'BTools', link: '/docc/BTools.md' },
          { text: '蓝图开发模式', link: '/docc/Blueprint.md' },
          { text: 'Vitepress搭建记录', link: '/docc/Vitepress.md' },
          { text: 'Docker部署记录',link:'/docc/docker.md'},
          { text: 'App主路由', link: '/docc/app.md' },
          { text: '路由模块', link: '/docc/routes.md' },
          { text: '样式风格', link: '/docc/style.md' },
          { text: '功能模块', link: '/docc/utils.md' },
        ]
      }
    ],
```



### 多样化操作

> 主要列一下我经常使用的一些方案

- 支持emoji
- 支持目录表

```markdown
[[TOC]]
```

- GitHub风格警报

```markdown
> [!NOTE]
> 强调用户在快速浏览文档时也不应忽略的重要信息。

> [!TIP]
> 有助于用户更顺利达成目标的建议性信息。

> [!IMPORTANT]
> 对用户达成目标至关重要的信息。

> [!WARNING]
> 因为可能存在风险，所以需要用户立即关注的关键内容。

> [!CAUTION]
> 行为可能带来的负面影响。
```

![image-20241205184120121](https://gitee.com/bx33661/image/raw/master/path/image-20241205184120121.png)

- 代码高亮
- ....
