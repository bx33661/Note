`WEB-INF` 是 Java Web 应用程序中一个重要的目录，它位于 Web 应用的根目录下，主要用于存储与 Web 应用相关的配置信息和资源。它遵循 Java Servlet 规范。

### 目录结构

一个典型的 Java Web 应用程序的目录结构如下：

```
MyWebApp/
├── index.html
├── css/
│   └── style.css
├── js/
│   └── script.js
├── images/
│   └── logo.png
├── WEB-INF/
│   ├── web.xml
│   ├── classes/
│   │   └── com/example/MyServlet.class
│   ├── lib/
│   │   └── some-library.jar
```

### `WEB-INF` 目录的内容

- **`web.xml`**: 这是 Web 应用程序的部署描述文件（Deployment Descriptor）。它包含 Web 应用程序的配置，例如：

  - URL 到 Servlet 的映射。
  - 过滤器（Filters）的定义。
  - 安全性配置。
  - 会话配置等。

  > 注：从 Servlet 3.0 开始，可以使用注解（如 `@WebServlet`）代替 `web.xml`。

- **`classes/`**: 存放编译后的 Java 类文件，通常是自定义的 Servlet 类、监听器类等。目录结构需要遵循 Java 包的命名规则。例如，`com.example.MyServlet` 的类文件应该放在 `classes/com/example/MyServlet.class`。

- **`lib/`**: 存放应用程序依赖的 JAR 文件，例如第三方库或工具。

### `WEB-INF` 的作用

1. **安全性**: `WEB-INF` 目录及其内容不能通过浏览器直接访问。这种限制使得应用程序的内部实现（如类文件、配置文件和依赖库）被保护，不会暴露给用户。
2. **应用配置**: `WEB-INF` 是 Web 容器（如 Tomcat、Jetty 等）用来识别和加载 Web 应用程序配置的目录。Web 容器启动时会读取 `web.xml` 中的配置来初始化应用。
3. **类和库加载**: 应用程序的类和库文件会存放在 `WEB-INF/classes` 和 `WEB-INF/lib` 中，这些资源会被 Web 容器的类加载器加载，以供应用程序运行。

### 注意事项

- 虽然 `WEB-INF` 本身是不可直接访问的，但可以通过应用的代码间接使用其中的资源。
- 使用现代 Java Web 框架（如 Spring Boot），传统的 `WEB-INF` 目录已不再需要，因为框架通常会提供更简化的部署方式（例如嵌入式容器）。