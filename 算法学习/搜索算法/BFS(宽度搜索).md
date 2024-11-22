# BFS(宽度搜索)

----

求最短路问题时，需要保证所有格子的权重是一样的

## 走迷宫

![image-20240530114002378](https://gitee.com/bx33661/image/raw/master/path/image-20240530114002378.png)



```cpp
#include <bits/stdc++.h>
using namespace std;
const int N = 110;
typedef pair<int, int> PII;
int dx[] = {-1, 0, 1, 0}, dy[] = {0, 1, 0, -1};
int g[N][N], dist[N][N], n, m;
PII q[N * N];

int bfs() {
    memset(dist, -1, sizeof dist);
    dist[0][0] = 0;
    int hh = 0, tt = 0;
    q[0] = {0, 0};
    
    while (hh <= tt) {
        PII t = q[hh ++ ];
        for (int i = 0; i < 4; ++ i) {
            int a = t.first + dx[i], b = t.second + dy[i];
            if (a < 0 || a >= n || b < 0 || b >= m || ~dist[a][b] || g[a][b])
                continue;
            dist[a][b] = dist[t.first][t.second] + 1;
            q[ ++ tt] = {a, b};
        }
    }
    
    return dist[n - 1][m - 1];
}

int main() {
    scanf("%d%d", &n, &m);
    for (int i = 0; i < n; ++ i)
        for (int j = 0; j < m; ++ j)
            scanf("%d", &g[i][j]);
            
    printf("%d\n", bfs());
    
    return 0;
}
```



```
#include <bits/stdc++.h>
#include "queue"
using namespace std;
const int N = 110;
typedef pair<int, int> PII;
int dx[] = {-1, 0, 1, 0}, dy[] = {0, 1, 0, -1};
/*
 * dx[] = {-1, 0, 1, 0}
 * dy[] = {0, 1, 0, -1}
 *        实现左下右上遍历
 * */
int g[N][N], dist[N][N], n, m; //g用来储存图，
PII q[N * N];//用来模拟队列

int bfs() {
    memset(dist, -1, sizeof dist);
    dist[0][0] = 0;
    int hh = 0, tt = 0;
    q[0] = {0, 0};

    while (hh <= tt) { //hh 和 tt 是用来管理队列的两个变量，它们分别代表队列的头（head）和尾（tail）。
                      //把整张图的所有部分都要扫描一遍
        PII t = q[hh ++ ];

        for (int i = 0; i < 4; ++ i) {
            int a = t.first + dx[i], b = t.second + dy[i];
            if (a < 0 || a >= n || b < 0 || b >= m || ~dist[a][b] || g[a][b])
                /*通过 ~dist[a][b] 的按位取反，以下是几种情况：
                如果 dist[a][b] 是 -1，那么 ~dist[a][b] 的结果是 0，条件 ~dist[a][b] 为假。
                如果 dist[a][b] 不是 -1，那么 ~dist[a][b] 将是一个非零值，条件 ~dist[a][b] 为真。
                 * */
                continue;
            dist[a][b] = dist[t.first][t.second] + 1;
            q[ ++ tt] = {a, b}; // 将新节点添加到队列尾部，并将 tt 增加 1
        }
    }

    return dist[n - 1][m - 1];
}

int main() {
    //输入输出流
    scanf("%d%d", &n, &m);
    for (int i = 0; i < n; ++ i)
        for (int j = 0; j < m; ++ j)
            scanf("%d", &g[i][j]);

    printf("%d\n", bfs());

    return 0;
}
```



### memset()函数

`memset` 函数是 C++ 标准库中的一个函数，用于将某一特定值设置到一块内存区域。这个函数通常用于初始化数组或结构体中的内存，使其内容设置为一个指定的字节值。

`memset` 函数的原型定义在头文件 `<cstring>` 中，其原型如下：

```
cpp
复制代码
void* memset(void* ptr, int value, size_t num);
```

各个参数的含义如下：

- `ptr`：指向要被设置的内存块的指针。
- `value`：要设置的值（以 `int` 类型传递，但实际使用的是其低位字节）。
- `num`：要设置的字节数。

`memset` 函数返回一个指向内存区域 `ptr` 的指针。



