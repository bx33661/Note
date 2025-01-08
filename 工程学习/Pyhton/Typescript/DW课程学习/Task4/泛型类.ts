//泛型类
class GenericBox<T> {
    private _content: T;

    constructor(content: T) {
        this._content = content;
    }

    public getContent(): T {
        return this._content;
    }

    public setContent(content: T): void {
        this._content = content;
    }
}

// 使用泛型类
let stringBox = new GenericBox<string>('Hello, World!');
console.log(stringBox.getContent()); // Hello, World!

let numberBox = new GenericBox<number>(123);
console.log(numberBox.getContent()); // 123