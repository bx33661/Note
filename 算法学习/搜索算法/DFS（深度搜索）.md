## DFS（深度搜索）

---

DFS是一条路走到黑



## 全排列问题

```cpp
//DFS
// Created by lenovo on 2024/5/27.
//全排列问题
#include "iostream"
using namespace std;

const int N = 100;
int path[N];    //保存数据节点
bool st[N];     //判断是否被使用，一个状态数组
int n;

void dfs(int u){
    if(u==n){
        //如果达到第u层则输出退出
        for (int i = 0; i < n; ++i) {
            printf("%d",path[i]);
        }
        printf("\n");
        return;
    }
    for (int i = 1; i <= n; ++i) {
        if (!st[i]) {
            path[u] = i;    
            st[i] = true;

            dfs(u + 1);     //向下搜索

            st[i] = false;    //恢复原来的状态
            //path[u]=0;
        }
    }
}

int main(){
    cin>>n;
    dfs(0);
    return 0;
}
```



---

## n皇后问题

```cpp
//BFS
// Created by lenovo on 2024/5/27.
//n皇后问题
#include "iostream"
using namespace std;
const int N=20;
int n;
char g[N][N];
bool col[N],dg[2*N],udg[2*N];

void dfs(int u){
    if(u==n){
        for (int i = 0; i < n; ++i) {
            puts(g[i]);
        }
        puts("");
        return;
    }

    for (int i = 0; i < n; ++i) {
        if (!col[i]&&!dg[u+i]&&!udg[u-i+n]){
            g[u][i] ='Q';
            col[i]=dg[u+i]=udg[u-i+n]= true;
            dfs(u+1);
            col[i]=dg[u+i]=udg[u-i+n]= false;
            g[u][i] ='.';
        }
    }
}

int main(){
    cin>>n;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            g[i][j]='.';
        }
    }

    dfs(0);
    return 0;
}
```

### 对于坐标的操作：

1. **`col[i]`**: 用于标记第`i`列是否有皇后。
2. **`dg[u + i]`**: 用于标记主对角线是否有皇后。主对角线的特点是所有在同一主对角线上的位置满足行号和列号之和相等，例如`(u, i)`位置的主对角线编号是`u + i`。
3. **`udg[u - i + n]`**: 用于标记副对角线是否有皇后。副对角线的特点是所有在同一副对角线上的位置满足行号和列号之差相等，例如`(u, i)`位置的副对角线编号是`u - i + n`。这里加上`n`是为了避免负数索引。

### 第二种方法

```cpp
#include "iostream"
using namespace std;
const int N=20;
int n;
char g[N][N];       //记录数据
bool col[N],dg[2*N],udg[2*N],row[N];

void dfs(int x,int y,int s){  
    /**整体思路大概是一行一行地检查
     * 确保所有格子都被遍历，实现所有的可能
     * */
    //x记录当前的行数，y记录当前的列数，s记录放的皇后数量
    if (y==n) y=0,x++;        //当y超过当前的列数的时候，去到下一行
    if (x==n){                //如果行号x超出范围，检查是否放置了n个皇后，如果是，则打印棋盘并返回
        if (s==n){            //检查是否放完了所有的皇后
            for (int i = 0; i < n; ++i) {
                puts(g[i]);         //执行打印
                printf("\n");
            }
            return;
        }
    }
    //不放皇后
    dfs(x,y+1,s);

    //放皇后
    if(!row[x]&&!col[y]&&!dg[x+y]&&!udg[x-y+n]){
        g[x][y] = 'Q';
        row[x]=col[y]=dg[x+y]=udg[x-y+n] = true;
        dfs(x,y+1,s+1);
        row[x]=col[y]=dg[x+y]=udg[x-y+n] = false;
        g[x][y] ='.';
    }

}

int main(){
    cin>>n;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            g[i][j]='.';
        }
    }

    dfs(0,0,0);
    return 0;
}
```

