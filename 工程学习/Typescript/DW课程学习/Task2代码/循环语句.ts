//循环语句
/*
for (let i =0;i<10;i++){
    console.log(i)
}
*/

//实现阶乘
let num:number = 5
let result:number = 1
for(let i=1;i<=num;i++){
    result *=i
}
//console.log(result)
/*
let nums = [1,2,3,4,5]
for (let i in nums){
    console.log(i)
}
*/

let nums = [1,2,3,4,5]
for (let i of nums){
    console.log(i)
}
