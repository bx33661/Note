//泛型
function identity<T>(arg:T):T {
    return arg;
}

let output = identity<string>('myString');
console.log(output); // myString
let output2 = identity<number>(100);
console.log(output2); // 100