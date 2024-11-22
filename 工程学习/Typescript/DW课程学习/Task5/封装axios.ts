import axios from 'axios';

const service = axios.create({
    baseURL: 'http://api.bx33661.com',
    timeout:  5000,
    headers: {
        'Content-Type': 'application/json'
    }
});

service.interceptors.request.use(
    config => {
        return config;
    },
    error => {
        return Promise.reject(error);
    }
);

service.interceptors.response.use(response => {
    const res = response.data;
    if (res.code !== 200) {
        return res.data;
    }else {
        return Promise.reject(new Error(res.message));
    }
}, error => {
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