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