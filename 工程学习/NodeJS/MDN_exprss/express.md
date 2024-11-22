### npm

> NPM 手动逐个安装所需包。但通常可用 [package.json](https://docs.npmjs.com/files/package.json) 文件来管理依赖

我们可以来看到`express`的package.json

```json
{
  "dependencies": {
    "express": "^4.21.1"
  }
}
```



项目结构：

```
/express-locallibrary-tutorial
    app.js
    /bin
        www
    package.json
    /node_modules
        [约 4,500 个子文件夹和文件]
    /public
        /images
        /javascripts
        /stylesheets
            style.css
    /routes
        index.js
        users.js
    /views
        error.pug
        index.pug
        layout.pug
```

