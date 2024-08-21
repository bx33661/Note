# SQL注入

----

> SQL注入（SQL Injection），是指攻击者通过在Web应用的输入字段中输入恶意的SQL代码，从而欺骗服务器执行非预期的SQL命令的一种攻击方式。这种行为可以绕过服务器的安全机制，非法读取、修改、删除数据库中的数据，甚至有可能控制数据库管理系统（DBMS）。

联合注入基本流程：

1. 判断注入类型
2. 查列数
3. 确定字段位置
4. 查表名称
5. 查列名称
6. 获取目标数据

## sql中几个知识

### sql注释

在SQL中，注释符号用于添加说明或注释，使代码更易于理解，或者在调试过程中临时禁用某些SQL语句的部分。以下是SQL中常用的注释符号：

1. 单行注释：

   - `--`：在行尾使用两个连字符开始注释。任何在`--`之后的文本都会被视为注释，直到行尾。
     示例：

   ```sql
   SELECT * FROM users; -- 这是一条注释
   ```

   - `#`符号也可以用来表示单行注释，这是特定于某些数据库管理系统的，比如 MySQL、MariaDB、SQLite 和 PostgreSQL。使用`#`符号开始的注释会持续到该行末尾。

     以下是一个使用`#`符号进行注释的示例：

     ```sql
     SELECT * FROM users; # 这是一条注释
     ```

     在这个例子中，`#`之后的所有内容都会被视为注释。

2. 多行注释：

   - `/* ... */`：使用`/*`开始注释，并使用`*/`结束注释。这种注释可以跨越多行。
     示例：

   ```sql
   /* 这是一条
      多行注释 */
   SELECT * FROM users;
   ```

   注释在SQL代码中非常有用，尤其是在复杂的查询或存储过程中，它们可以帮助其他开发者（或未来的你）更快地理解代码的意图。然而，需要注意的是，在生产环境中，不应该在SQL查询中留下详细的注释，因为这可能会泄露敏感信息或业务逻辑。

### 报错类型判断数据库类型

- **ORACLE**
  ORA-01756:quoted string not properly terminated
  ORA-00933:SQLcommand not properly ended

- **MS-SQL**
  Msg 170,level 15, State 1,Line 1
  Line 1:Incorrect syntax near ‘foo
  Msg 105,level 15,state 1,Line 1
  Unclose quotation mark before the character string ‘foo

- **MYSQL**
  you have an error in your SQL syntax,check the manual that corresponds to you mysql server version for the right stntax to use near ‘’foo’ at line x

```sql
select id,name from users where id = $id
```

几种类型：

```sql
select id,name from users where id = 1;
select id,name from users where id = '1';
select id,name from users where id = "1";
select id,name from users where id = (1);
```

如果在后面添加一个` '`，如果报错排除双引号的的情况！:

```sql
select id,name from users where id = 1';    #报错
select id,name from users where id = '1'';	#报错

select id,name from users where id = "1'";  #正常

select id,name from users where id = (1');	#报错
```

- 可以先尝试什么都没有
-  在后面添加一个` '#`

如果成功说明是 ' ' 包括，

- 接着可以尝试添加框号` ')#`

可以尝试是否是`('')`形式，若不成功，可以继续尝试框号的多层嵌套，但一般不会超过两层框号的形式

- 尝试`)#`

若操作成功，不报错，可以说明，是` ($id)`的形式

- 在此基础上在后面继续添加一个 ` and '1 `

```sql
select id,name from users where id = 1' and '1;    报错

select id,name from users where id = '1'and '1';	正常

select id,name from users where id = (1' and '1);	
```

> `#` === `%23`

### `--+`替代`#`和`%23`

在SQL中，`--+` 是一种特殊的注释符号用法，它主要用于某些SQL注入攻击中。这种注释方式通常用于在URL参数或Web表单输入中注入SQL代码时，绕过应用程序的过滤机制。

具体来说，`--+` 的作用如下：

- `--` 是SQL中用来表示单行注释的开始。
- `+` 在某些情况下，如果输入被作为URL编码的一部分，`+` 可能会被Web服务器解码为空格字符。

因此，当攻击者在一个输入字段中插入类似 `id=10--+` 的字符串时，如果Web应用程序没有正确地处理或转义这个输入，那么在服务器端生成的SQL查询可能会变成：

```sql
SELECT * FROM users WHERE id = 10 --+ [其他代码]
```

在这里，`--+` 之后的所有内容都会被视为注释，从而可能被忽略。这样，攻击者可以有效地禁用查询的某些部分，比如关闭一个 `WHERE` 子句或一个 `LIMIT` 子句，以操纵SQL查询的结果。

需要注意的是，这并不是SQL语言的标准注释用法，而是一种利用特定环境下的漏洞进行的攻击手段。为了防止SQL注入攻击，开发者应该始终使用参数化查询、预编译语句、适当的输入验证和转义，并确保应用程序代码不会直接将用户输入拼接到SQL查询中。

## 查列数

```sql
select id,username union select 1,2

select 1,2 union select 1,2,3  
# The used SELECT statements have a different number of columns
```

第二句会报错，因为两个结果集列数不同！

### 使用`order by`

> `ORDER BY` 是SQL查询语句中的一个子句，用于对查询结果集进行排序。它可以按照一个或多个列进行排序，并且可以指定排序的方向，即升序（ASC）或降序（DESC）。
>
> 以下是 `ORDER BY` 的基本用法：
>
> ### 基本语法
>
> ```sql
> SELECT column1, column2, ...
> FROM table_name
> ORDER BY column1 ASC|DESC, column2 ASC|DESC, ...;
> ```
>
> ### 示例
>
> 假设我们有一个名为 `employees` 的表，包含以下列：`id`, `first_name`, `last_name`, 和 `salary`。
>
> #### 单列排序
>
> 按照 `last_name` 列升序排序：
>
> ```sql
> SELECT * FROM employees ORDER BY last_name ASC;
> ```
>
> #### 多列排序
>
> 首先按照 `last_name` 列升序排序，然后按照 `first_name` 列降序排序：
>
> ```sql
> SELECT * FROM employees ORDER BY last_name ASC, first_name DESC;
> ```
>
> #### 按照表达式排序
>
> 按照 `salary` 列的倍数进行排序：
>
> ```sql
> SELECT * FROM employees ORDER BY salary * 0.9 DESC;
> ```
>
> #### 按照列的位置排序
>
> 可以使用列的位置（基于 `SELECT` 子句中的位置）进行排序，这在列名较长或不确定时很有用：
>
> ```sql
> SELECT id, first_name, last_name, salary FROM employees ORDER BY 4 DESC;
> ```
>
> 在上面的查询中，`4` 表示 `SELECT` 子句中的第四列，即 `salary`。
>
> ### 注意事项
>
> - `ASC` 表示升序排序，这是默认的排序方式，即使不明确指定，也会按照升序排序。
> - `DESC` 表示降序排序。
> - 如果 `ORDER BY` 子句中的列名有歧义（例如，如果表使用了联接，并且多个表中都有相同的列名），则应指定列的前缀，例如 `table_name.column_name`。
> - 在某些数据库系统中，如果排序的列包含 `NULL` 值，则 `NULL` 值通常被视为最小值，在升序排序时出现在最前面，在降序排序时出现在最后面。
>
> 使用 `ORDER BY` 子句是数据库操作中常见的做法，尤其是在需要对数据进行展示或分析时。

```sql
select * from users order by 10 
# Unknown column '10' in 'order clause
```

利用报错，来逐步确定列数！！

## 确定字段位置

## 查表名和列名

### 获取数据库的信息

```sql
database() # 查看当前数据库
version() # 查看数据库版本信息
user() # 查看当前数据库连接的用户
```

> 系统数据库：
>
> MySQL安装时会自动创建几个系统数据库，这些数据库对于MySQL服务器的运行和管理至关重要。以下是MySQL中常见的系统数据库及其用途：
>
> 1. `mysql`：
>    - 这个数据库是MySQL的核心，它存储了用户账户信息、权限设置、关键字缓存、事件、存储过程、函数、触发器、服务器端帮助信息和时区数据等。
>    - `mysql` 数据库中的表通常以 `mysql` 前缀开头，例如 `user`、`db`、`table`、`columns`、`procs` 等。
> 2. `information_schema`：
>    - 这个数据库是一个虚拟数据库，提供了访问服务器上所有其他数据库元数据（即关于数据的数据）的能力。
>    - 它包含了多个只读表，这些表可以用来查询关于数据库、表、列、权限和其他各种对象的信息。
>    - 常用的表包括 `tables`、`columns`、`statistics`、`user_privileges` 等。
> 3. `performance_schema`：
>    - 这个数据库是MySQL 5.5及以上版本的一部分，提供了用于监控MySQL服务器运行时性能的设施。
>    - 它包含了一系列表和视图，可以用来查看服务器事件、锁定、I/O、内存使用情况、事务、存储引擎操作等。
> 4. `sys`：
>    - `sys` 数据库是MySQL 5.7及以上版本的一部分，它基于 `performance_schema` 数据库提供了一系列视图，使得查询性能相关的信息更加容易。
>    - 这个数据库提供了格式化的和易于理解的性能数据，对于性能调优和诊断非常有用。
>
> 这些系统数据库对于维护MySQL实例的稳定性和安全性至关重要。在管理MySQL服务器时，应该谨慎操作这些数据库，特别是 `mysql` 数据库，因为任何不当的更改都可能导致服务器无法正常运行。通常，不建议直接修改 `information_schema` 和 `performance_schema` 数据库中的数据，因为这些数据库中的数据是由MySQL服务器管理的。

```sql
select table_name from information_schema.tables where table_schema='xxx'
```

如此我们得到flag的表名

```sql
select column_name from information_schema.columns where table_name='xxx'
```



最后查询该表该列

```sql
select column_name from table_name;
```

