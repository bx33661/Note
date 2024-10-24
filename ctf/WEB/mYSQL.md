https://juejin.cn/post/7190306988939542585#heading-52

[TOC]

### desc命令

> 显示表的列信息。这个命令可以让你快速查看表结构，包括列名、数据类型、是否允许为空、是否有默认值等信息

```sql
DESC students;
#可以使用替换
SHOW COLUMNS FROM table_name;
```

示例：

```sql
mysql> desc students;
+--------+-------------+------+-----+---------+----------------+
| Field  | Type        | Null | Key | Default | Extra          |
+--------+-------------+------+-----+---------+----------------+
| id     | int         | NO   | PRI | NULL    | auto_increment |
| name   | varchar(50) | YES  |     | NULL    |                |
| course | varchar(50) | YES  |     | NULL    |                |
+--------+-------------+------+-----+---------+----------------+
3 rows in set (0.01 sec)
```

### 创建表

基本语法：

```sql
CREATE TABLE table_name (
    column1_name column1_type column1_constraints,
    column2_name column2_type column2_constraints,
    ...
    table_constraints
);
```

例子：

```sql
create table student(
		id int ,
		name varchar(10),
		gender char(1),
		birthday date,
		score double(5,2) ,
		addr varchar(50),
		status tinyint
);
```

**常见的数据类型：**

- **int**: 整数
- **varchar(n)**: 可变长度字符串，最大长度为 n
- **char(n)**: 固定长度字符串，长度为 n
- **text**: 较长的文本
- **datetime**: 日期和时间
- **date**: 日期
- **time**: 时间
- **float**: 浮点数
- **decimal(p, s)**: 精确数值，p 表示总位数，s 表示小数位数

**常见的约束条件**

- **NOT NULL**: 不允许为空
- **DEFAULT value**: 默认值
- **PRIMARY KEY**: 主键
- **UNIQUE**: 唯一值
- **FOREIGN KEY**: 外键
- **AUTO_INCREMENT**: 自动递增（通常用于主键）

**一个复杂的例子：**

```sql
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT,
    gender CHAR(1),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE courses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    student_id INT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(id)
);
```



### 修改表

修改表名：

```sql
alter table 表名 rename to 新的表名;
```

增加一列：

```sql
alter table 表名 add 列名 数据类型;
```

修改数据类型：

```sql
alter table 表名 modify 列名 新数据类型;
```

修改列名和数据类型：

```sql
alter table 表名 change 列名 新列名 新数据类型;
```

删除列：

```sql
alter table 表名 drop 列名;
```



### 更新/更改数据

```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

- `table_name`：要更新的表的名称。
- `SET`：指定要更新的列及其新值。
- `WHERE`：指定哪些记录需要更新。如果不使用`WHERE`子句，所有的记录都将被更新。

### 查询

> 在MySQL中，使用反引号（```）可以确保表名和列名在查询时不会与SQL关键字冲突，也可以确保它们被正确解析。尤其是在表名或列名包含特殊字符或空格时，使用反引号是必要的。
>
> 在MySQL中，字符串值需要用单引号（`'`）

#### 基础查询

```sql
select name,math from stu;
```

```sql
select * from stu;
```



#### 条件查询

> MySQL默认情况下对表名和列名不区分大小写，
>
> 但对字符串值是区分大小写的。除非你明确设置了数据库的大小写敏感性

```sql
select 字段列表 from 表名 where 条件列表;
```

在MySQL中，条件查询是通过 `SELECT` 语句结合 `WHERE` 子句来实现的。`WHERE` 子句用于指定查询条件，从而从表中筛选出符合特定条件的记录。以下是一些常见的条件查询示例和用法。

**基本语法**

```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

where 语句------常常需要配合各种操作符号使用

常见的条件操作符

1. **等于（=）**
2. **不等于（<> 或 !=）**
3. **大于（>）**
4. **小于（<）**
5. **大于等于（>=）**
6. **小于等于（<=）**
7. **BETWEEN ... AND ...**: 介于两个值之间
8. **IN (value1, value2, ...)**: 在指定的值列表中
9. **LIKE 'pattern'**: 模式匹配
10. **IS NULL**: 判断是否为NULL
11. **IS NOT NULL**: 判断是否不为NULL
12. **AND**: 逻辑与
13. **OR**: 逻辑或
14. **NOT**: 逻辑非

示例

假设我们有一个 `students` 表，结构如下：

```sql
CREATE TABLE `students` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(100) NOT NULL,
    `age` INT,
    `gender` CHAR(1),
    `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO `students` (`name`, `age`, `gender`) VALUES
('Alice', 20, 'F'),
('Bob', 22, 'M'),
('Charlie', 21, 'M'),
('Diana', 20, 'F'),
('Eva', 23, 'F');
```

1. 等于（=）

查询年龄为20岁的学生：

```sql
SELECT * FROM `students` WHERE `age` = 20;
```

2. 不等于（<> 或 !=）

查询年龄不为20岁的学生：

```sql
SELECT * FROM `students` WHERE `age` != 20;
```

大于（>）和小于（<）

查询年龄大于20岁的学生：

```sql
SELECT * FROM `students` WHERE `age` > 20;
```

查询年龄小于22岁的学生：

```sql
SELECT * FROM `students` WHERE `age` < 22;
```

4. 大于等于（>=）和小于等于（<=）

查询年龄大于等于21岁的学生：

```sql
SELECT * FROM `students` WHERE `age` >= 21;
```

查询年龄小于等于22岁的学生：

```sql
SELECT * FROM `students` WHERE `age` <= 22;
```

5. BETWEEN ... AND ...

查询年龄在20到22岁之间的学生：

```sql
SELECT * FROM `students` WHERE `age` BETWEEN 20 AND 22;
```

6. IN (value1, value2, ...)

查询名字为 'Alice' 或 'Bob' 的学生：

```sql
SELECT * FROM `students` WHERE `name` IN ('Alice', 'Bob');
```

7. LIKE 'pattern'

查询名字以 'A' 开头的学生：

```sql
SELECT * FROM `students` WHERE `name` LIKE 'A%';
```

查询名字包含 'i' 的学生：

```sql
SELECT * FROM `students` WHERE `name` LIKE '%i%';
```

8. IS NULL 和 IS NOT NULL

查询性别为NULL的学生：

```sql
SELECT * FROM `students` WHERE `gender` IS NULL;
```

查询性别不为NULL的学生：

```sql
SELECT * FROM `students` WHERE `gender` IS NOT NULL;
```

9. AND 和 OR

查询年龄为20岁且性别为女性的学生：

```sql
SELECT * FROM `students` WHERE `age` = 20 AND `gender` = 'F';
```

查询年龄为20岁或性别为女性的学生：

```sql
SELECT * FROM `students` WHERE `age` = 20 OR `gender` = 'F';
```

10. NOT

查询名字不为 'Alice' 的学生：

```sql
SELECT * FROM `students` WHERE NOT `name` = 'Alice';
```

复合条件

你还可以组合多个条件来进行更复杂的查询。例如，查询年龄在20到22岁之间且性别为女性的学生：

```sql
SELECT * FROM `students` WHERE `age` BETWEEN 20 AND 22 AND `gender` = 'F';
```



### 排序查询

````sql
select 字段列表 from 表名 order by 排序字段名1 [排序方式]...;
````

> 分别是升序ASC和降序DESC，默认情况下是升序ASC



### 聚合函数的利用

**常用的聚合函数**

1. **COUNT**: 计算行数
2. **SUM**: 计算总和
3. **AVG**: 计算平均值
4. **MIN**: 找到最小值
5. **MAX**: 找到最大值

好的，我理解了你的需求。为了更清晰地按照聚合函数的类型进行分类，我将聚合函数分为以下几类：计数、求和、平均值、最小值、最大值。每一类都会提供一些示例查询。

**1. 计数 (COUNT)**

计算表中的总行数

```sql
SELECT COUNT(*) AS total_students FROM `demo1`.`stu`;
```

计算非空行数

```sql
SELECT COUNT(math) AS total_math_scores FROM `demo1`.`stu`;
```

按性别分组计算学生人数

```sql
SELECT gender, COUNT(*) AS student_count
FROM `demo1`.`stu`
GROUP BY gender;
```

2. **求和 (SUM)**

计算所有学生的数学总分

```sql
SELECT SUM(math) AS total_math FROM `demo1`.`stu`;
```

计算所有学生的英语总分

```sql
SELECT SUM(english) AS total_english FROM `demo1`.`stu`;
```

按性别分组计算每个性别的数学总分

```sql
SELECT gender, SUM(math) AS total_math
FROM `demo1`.`stu`
GROUP BY gender;
```

按性别分组计算每个性别的英语总分

```sql
SELECT gender, SUM(english) AS total_english
FROM `demo1`.`stu`
GROUP BY gender;
```

3. **平均值 (AVG)**

计算所有学生的数学平均分

```sql
SELECT AVG(math) AS average_math FROM `demo1`.`stu`;
```

计算所有学生的英语平均分

```sql
SELECT AVG(english) AS average_english FROM `demo1`.`stu`;
```

按性别分组计算每个性别的数学平均分

```sql
SELECT gender, AVG(math) AS average_math
FROM `demo1`.`stu`
GROUP BY gender;
```

按性别分组计算每个性别的英语平均分

```sql
SELECT gender, AVG(english) AS average_english
FROM `demo1`.`stu`
GROUP BY gender;
```

按年龄分组计算每个年龄段的数学和英语平均分

```sql
SELECT age, AVG(math) AS average_math, AVG(english) AS average_english
FROM `demo1`.`stu`
GROUP BY age;
```

**4. 最小值 (MIN)**

找到所有学生的最低数学分

```sql
SELECT MIN(math) AS lowest_math FROM `demo1`.`stu`;
```

找到所有学生的最低英语分

```sql
SELECT MIN(english) AS lowest_english FROM `demo1`.`stu`;
```

按性别分组找到每个性别的最低数学分

```sql
SELECT gender, MIN(math) AS lowest_math
FROM `demo1`.`stu`
GROUP BY gender;
```

按性别分组找到每个性别的最低英语分

```sql
SELECT gender, MIN(english) AS lowest_english
FROM `demo1`.`stu`
GROUP BY gender;
```

5. **最大值 (MAX)**

找到所有学生的最高数学分

```sql
SELECT MAX(math) AS highest_math FROM `demo1`.`stu`;
```

找到所有学生的最高英语分

```sql
SELECT MAX(english) AS highest_english FROM `demo1`.`stu`;
```

按性别分组找到每个性别的最高数学分

```sql
SELECT gender, MAX(math) AS highest_math
FROM `demo1`.`stu`
GROUP BY gender;
```

按性别分组找到每个性别的最高英语分

```sql
SELECT gender, MAX(english) AS highest_english
FROM `demo1`.`stu`
GROUP BY gender;
```

处理NULL值

在计算平均值、总和等时，NULL值会被忽略。如果你需要将NULL值处理为0，可以使用 `COALESCE` 或 `IFNULL` 函数。

计算所有学生的英语平均分，将NULL值视为0

```sql
SELECT AVG(IFNULL(english, 0)) AS average_english
FROM `demo1`.`stu`;
```

计算所有学生的英语总分，将NULL值视为0

```sql
SELECT SUM(IFNULL(english, 0)) AS total_english
FROM `demo1`.`stu`;
```

附加示例

按性别和年龄分组计算每个组的学生人数

```sql
SELECT gender, age, COUNT(*) AS student_count
FROM `demo1`.`stu`
GROUP BY gender, age;
```

按性别分组计算每个性别的数学和英语分数标准差

```sql
SELECT gender, STDDEV(math) AS math_stddev, STDDEV(english) AS english_stddev
FROM `demo1`.`stu`
GROUP BY gender;
```

