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
