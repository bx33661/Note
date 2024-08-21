# sql 学习

[TOC]

----

> 数据库使用---MySQL，软件使用----Navicat Premium
>
> 学习地址：https://github.com/datawhalechina/wonderful-sql/

`SHOW DATABASES`查询到所有的数据库

![image-20240723150328560](C:/Users/lenovo/AppData/Roaming/Typora/typora-user-images/image-20240723150328560.png)

### 创建表

```sql
CREATE TABLE < 表名 >
( < 列名 1> < 数据类型 > < 该列所需约束 > < 默认设置 > ,
  < 列名 2> < 数据类型 > < 该列所需约束 > < 默认设置 > ,
  < 列名 3> < 数据类型 > < 该列所需约束 > < 默认设置 > ,
  < 列名 4> < 数据类型 > < 该列所需约束 > < 默认设置 > ,
  .
  .
  .
  < 该表的约束 1> , < 该表的约束 2> ,……);
```

本次课程的数据示例：

```sql
CREATE TABLE product
(product_id CHAR(4) NOT NULL,
 product_name VARCHAR(100) NOT NULL,
 product_type VARCHAR(32) NOT NULL DEFAULT "水果",
 sale_price INTEGER ,
 purchase_price INTEGER ,
 regist_date DATE ,
 PRIMARY KEY (product_id));
```

`SHOW TABLES`可以查询到所有的表

## 规范

### 命名规则：

- 只能使用半角英文字母、数字、下划线（_）作为数据库、表和列的名称
- 名称必须以半角英文字母开头

**通用命名规则：**

1. **字符限制**：名称通常以字母（A-Z，a-z）或下划线（_）开头，后续字符可以是字母、数字（0-9）或下划线。某些数据库系统可能还允许其他字符。
2. **长度限制**：大多数数据库系统对对象名称的长度有限制，通常是30个字符，但具体取决于具体的数据库系统。
3. **大小写敏感**：SQL本身不区分大小写，但某些数据库系统（如MySQL）默认情况下对表名和列名是大小写不敏感的，而其他系统（如PostgreSQL）则默认区分大小写。建议在命名时保持一致性。

**命名约定：**

1. **使用有意义的名称**：名称应该简洁且具有描述性，能够清楚地表示数据的内容或用途。
2. **使用驼峰命名法或下划线分隔**：驼峰命名法（CamelCase）或下划线分隔（snake_case）是两种常见的命名约定。
   - 驼峰命名法：例如 `firstName`, `lastName`
   - 下划线分隔：例如 `first_name`, `last_name`
3. **避免使用SQL关键字**：不要使用SQL保留字（如SELECT, FROM, WHERE等）作为对象名称，这可能会导致混淆或错误。
4. **保持一致性**：在整个数据库中保持一致的命名规则，以便于理解和维护。
5. **使用前缀或后缀**：有时会使用前缀或后缀来表示对象的类型或用途，例如：
   - 表：`tblCustomers`, `tblOrders`
   - 视图：`vwCustomerOrders`, `vwActiveUsers`
   - 存储过程：`spGetCustomer`, `spUpdateOrder`

**特定数据库系统的规则：**

- **MySQL**：默认情况下，表名和列名不区分大小写，但在Unix/Linux系统上，文件系统是区分大小写的，因此创建数据库和表时应该使用一致的大小写。
- **SQL Server**：对象名称默认是大小写不敏感的，但如果使用双引号（"）包围名称，则变为大小写敏感。
- **Oracle**：对象名称默认是大小写敏感的，但如果创建时使用了双引号，则可以包含大小写。
- **PostgreSQL**：对象名称默认是大小写敏感的，但如果创建时没有使用双引号，则会自动转换为小写。
遵循良好的命名规则可以提高数据库的结构清晰度和可维护性。不同的组织或项目可能会有自己的命名标准，因此在实际应用中，应该遵循组织内部的约定。