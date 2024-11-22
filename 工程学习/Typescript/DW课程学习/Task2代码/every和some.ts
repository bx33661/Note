//学习every和some

/*
const numbers = [1, 2, 3, 4, 5];
const hasEven = numbers.some(num => num % 2 === 0);
console.log(hasEven); // 输出: true

 */

const numbers = [1, 2, 3, 4, 5];
const evennumbers = [2,6,8,10]
//判断数组中是不是所有都是偶数
const hasEven = numbers.every(num => num % 2 === 0);
console.log(hasEven);
// 输出: false
const hasEven2 = evennumbers.every(num => num % 2 === 0);
console.log(hasEven2);