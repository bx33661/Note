 `META-INF/MANIFEST.MF` 文件，也就是 Manifest 文件。

**什么是 Manifest 文件？**

`MANIFEST.MF` 文件是 JAR 包中的一个特殊文件，它位于 `META-INF` 目录下。这个文件是一个纯文本文件，包含了关于 JAR 包自身的元数据信息，相当于 JAR 包的“身份证”或“配置文件”。它以键值对的形式存储信息，每行一个键值对，格式为 `键: 值`，键和值之间用冒号和空格分隔，例如：

```
Manifest-Version: 1.0
Created-By: 17.0.2 (Oracle Corporation)
Main-Class: com.example.Main
```

**Manifest 文件的主要作用：**

1. **描述 JAR 包的基本信息：** 包含 JAR 包的版本、创建者、构建日期等信息。
2. **指定应用程序的入口点：** 通过 `Main-Class` 属性指定 JAR 包中哪个类是应用程序的入口点，从而可以使用 `java -jar` 命令直接运行 JAR 包。
3. **管理 JAR 包的依赖关系：** 可以指定 JAR 包依赖的其他 JAR 包，即类路径（Classpath）。
4. **进行数字签名：** 可以包含 JAR 包的数字签名信息，用于验证 JAR 包的完整性和来源。
5. **其他扩展功能：** 可以包含一些自定义的属性，用于特定的应用程序或框架。

**Manifest 文件中常见的属性：**

- **`Manifest-Version`：** Manifest 文件的版本号，通常为 `1.0`。
- **`Created-By`：** 创建 JAR 包的工具和版本信息。
- **`Main-Class`：** 指定应用程序的入口类，当使用 `java -jar` 命令运行 JAR 包时，JVM 会执行这个类中的 `main` 方法。
- **`Class-Path`：** 指定 JAR 包依赖的其他 JAR 包的路径，多个路径之间用空格分隔。这些路径可以是相对于当前 JAR 包的相对路径，也可以是绝对路径或 URL。
- **`Implementation-Title`：** 定义扩展实现的标题。
- **`Implementation-Version`：** 定义扩展实现的版本。
- **`Implementation-Vendor`：** 定义扩展实现的组织。
- **`Implementation-Vendor-Id`：** 定义扩展实现的组织的标识。
- **`Specification-Title`：** 定义规范的标题。
- **`Specification-Version`：** 定义规范的版本。
- **`Specification-Vendor`：** 定义规范的组织。

**例子：**

假设我们有一个名为 `myapp.jar` 的 JAR 包，其中包含一个主类 `com.example.Main` 和一个工具类 `com.example.Utils`。`MANIFEST.MF` 文件可能如下所示：

```
Manifest-Version: 1.0
Created-By: 17.0.2 (Oracle Corporation)
Main-Class: com.example.Main
Class-Path: lib/mylib.jar otherlib.jar
```

这个 Manifest 文件表示：

- Manifest 文件的版本是 `1.0`。
- JAR 包是由 Oracle Corporation 的 JDK 17.0.2 创建的。
- 应用程序的入口类是 `com.example.Main`。
- JAR 包依赖于 `lib` 目录下的 `mylib.jar` 和当前目录下的 `otherlib.jar`。

**如何创建和修改 Manifest 文件：**

1. **手动创建：** 你可以使用任何文本编辑器创建一个名为 `MANIFEST.MF` 的文件，并按照键值对的格式编写内容。
    
2. **使用 `jar` 命令：** 使用 `jar` 命令创建 JAR 包时，可以通过 `-m` 选项指定一个包含 Manifest 信息的文本文件。例如：
    
    Bash
    
    ```
    jar cvfm myapp.jar manifest.txt *.class
    ```
    
    其中 `manifest.txt` 就是包含 Manifest 信息的文本文件。
    
3. **使用构建工具：** Maven 和 Gradle 等构建工具会自动生成 `MANIFEST.MF` 文件，并允许你通过配置来修改其中的属性。
    

**总结：**

`MANIFEST.MF` 文件是 JAR 包中非常重要的组成部分，它包含了 JAR 包的元数据信息，方便了 JAR 包的管理、部署和使用。理解 Manifest 文件的作用和格式对于 Java 开发者来说很有帮助。