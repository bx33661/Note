let num1:number = 5

//if-else if-else语句
if(num1<10){
    console.log("small number")
}else if(num1>=10&&num1<=100){
    console.log("medium number")
}else {
    console.log("large number")
}

//switch-case 语句
switch (num1) {
    case 1:
        console.log("数字的值为1")
        break
    case 2:
        console.log("数字的值为2")
        break
    case 3:
        console.log("数字的值为3")
        break
    default:
        console.log("Not found")
        break
}