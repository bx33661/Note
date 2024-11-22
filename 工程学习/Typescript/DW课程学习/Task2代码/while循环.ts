//while循环学习
//斐波那契数列
function fibonacci(n: number): number {
  let a:number = 1
  let b:number = 1
  while (n > 2) {
    let temp = a + b;
    a = b;
    b = temp;
    n--;
  }
  return b;
}
//let result:number = fibonacci(5);
console.log(result)