# TypeScript-- 第五章

---

<img src="https://gitee.com/bx33661/image/raw/master/path/typescript-logo.png" alt="TypeScript(nodejs)のimport時の挙動" style="zoom:67%;" />

> DataWhale:https://github.com/bx33661/TS-/tree/main/tutorial/TypeScript/%E7%AC%AC5%E7%AB%A0-ts%E9%AB%98%E7%BA%A7%E5%86%85%E5%AE%B9
>
> Author:bx33661​

## 异步处理

与js差不多

> 在 TypeScript 中处理异步操作时，主要通过 `async/await` 语法和 `Promise` 来实现,`Promise` 对象代表一个最终会完成（以一个值成功）或者失败，并且一旦状态改变就无法再改变的异步操作的结果。

一个`Promise` 例子：

```typescript
const promiseExample = new Promise<string>((resolve, reject) => {
    setTimeout(() => {
        resolve('Promise fulfilled');
    }, 2000);
});

promiseExample.then(result => {
    console.log(result);
}).catch(error => {
    console.error(error);
});
```

`async` 和 `await` 语法

> `async/await` 是在 `Promise` 基础上的一层抽象，它可以让异步代码看起来和同步代码很相似，使得代码更加可读和直观。一个使用 `async` 声明的函数会隐式地返回一个 `Promise`

```ts
async function apirearch() {
    const res = await fetch('https://api.bx33661.com/');
    const data = await res.json();
    return
}

apirearch().then(res => {
    console.log(res)
}).catch(err => {
    console.error('Error:', err)
})
```

*注意：`await` 只能在 `async` 函数内部使用*

这个例子中使用到了`then` 和 `catch`

- `then` 方法用于处理一个成功完成的 `Promise`，即当 `Promise` 的状态变为“已解决”（fulfilled）时调用的方法
- `catch` 方法用于处理 `Promise` 的拒绝状态（rejected）



这里我们模拟一下请求出错的情况：

```ts
const promiseThatMayFail = new Promise((resolve, reject) => {
    setTimeout(() => {
        // 这里模拟网络请求失败
        reject(new Error('Server error'));
    }, 2000);
});

promiseThatMayFail
    .then(result => {
        console.log('Success:', result);
    })
    .catch(error => {
        console.error('Error caught:', error);
    });

```

```ts
Error caught: Error: Server error
    at Timeout._onTimeout (e:\gitproject\Typescript\ts%E7%89%B9%E6%80%A7\%E6%A8%A1%E6%8B%9F%E7%BD%91%E7%BB%9C%E5%87%BA%E9%94%99.ts:4:16)
```



链式调用，让程序更具流程

```ts
fetch('https://api.example.com/data')
    .then(response => response.json())
    .then(json => console.log(json))
    .catch(console.error);
```

感觉在WEB开发中的时候，这种异步操作是很有必要的，无需等待一些传统的操作

在请求的时候，执行其他任务，提高效率



## `GET` 和 `POST`请求

> 官网介绍：Vite（法语意为 "快速的"，发音 `/vit/`，发音同 "veet"）是一种新型前端构建工具，能够显著提升前端开发体验。
>
> https://cn.vitejs.dev/guide/

```shell
create-vite vue3ts --template vue-ts
cd vue3ts
npm install
npm run dev
```

![image-20240926193324433](https://gitee.com/bx33661/image/raw/master/path/image-20240926193324433.png)

```shell
#安装网络请求库axios
npm install axios
```

### 发起网络请求

Front-end->>

```vue
<template>
  <button @click="get_query()">发起GET请求</button>
</template>

<script setup lang='ts'>
import axios from 'axios'
// 发起GET请求
interface TestData {
message: string;
}
const get_query = ()=>{
axios.get<TestData>('http://127.0.0.1:8009/')
.then(response => {
  const testData: TestData = response.data;
  console.log(testData.message);
})
.catch(error => {
  console.error(error);
});
}
</script>
```

Back-end ->>(基于fastapi)

```python
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)
@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8009)
```

<img src="https://gitee.com/bx33661/image/raw/master/path/image-20240926224734965.png" alt="image-20240926224734965" style="zoom:50%;" />

发送GET请求：

![image-20240926224803244](https://gitee.com/bx33661/image/raw/master/path/image-20240926224803244.png)

## 封装axios

> 这个部分真的不太熟悉😭😭😭😭

跟着手敲一个封装实例：

```ts
//引入模块axios
import axios from 'axios';

//创建一个axios 的实例
const service = axios.create({
    baseURL: 'http://api.bx33661.com',
    timeout:  5000,
    headers: {
        'Content-Type': 'application/json'
    }
});

//请求拦截器是 Axios 提供的一种机制，它允许在请求过程中添加自定义的处理逻辑。请求拦截器会在发送请求之前执行，这可以被用于修改请求配置、添加请求头、显示加载动画等操作。
service.interceptors.request.use(
    config => {
        return config;
    },
    error => {
        return Promise.reject(error);
    }
);

//service.interceptors.response.use 是 Axios 中处理响应的拦截器。这部分代码定义在 Axios 发送请求并接收响应之后的行为，可以用来对响应数据进行统一处理，包括数据格式化、错误处理、重试策略等
service.interceptors.response.use(response => {
    const res = response.data;
    if (res.code !== 200) {//代表请求成功
        //返回信息
        return res.data;
    }else {
        return Promise.reject(new Error(res.message));
    }
}, error => {
    //接受一系列的错误参数
    if (error.response){
        switch (error.response.status) {
            case 400:
                break;
            case 401:
                break;
            case 403:
                break;
            case 404:
                break;
            case 500:
                break;
            default:
                break;
        }
    }
    return Promise.reject(error);
})

// 创建GET请求方法
export function get(url, params) {
    return new Promise((resolve, reject) => {
        service.get(url, { params }).then(response => {
            resolve(response);
        }).catch(error => {
            reject(error);
        });
    });
}

// 创建POST请求方法
export function post(url, data) {
    return new Promise((resolve, reject) => {
        service.post(url, data).then(response => {
            resolve(response);
        }).catch(error => {
            reject(error);
        });
    });
}

export default service;
```

> `export` 是一个关键字，用于从一个模块向外公开（或导出）其内部的函数、对象、类或变量等，使得其他模块可以使用这些定义
>
> 与`import`相对应，通俗点讲就是导出给别的文件用



在`type.ts`写接口类型：

```ts
export interface Login {
    username: string
    password: string
}

export interface API {
    id: number,//请求的数据，用泛型
    username: string, // 返回状态码的信息，如请求成功等
    email: string, //返回后端自定义的200，404，500这种状态码
    token: string, 
}
```



## 本地运行配置

```shell
#在项目下
npm install --save-dev @types/node
#编译成js文件
tsc filename.ts
#node运行js
node filename.js
```

> 在执行异步语句的时候需要拉去模块
>
> `TypeScript` 编译器默认使用 ES5 标准，而 ES5 标准中不包含 Promise 对象。async/await 是 ES2017（也称为 ES8）的特性