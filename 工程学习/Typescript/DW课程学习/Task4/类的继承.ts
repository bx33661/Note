//类的继承
class language {
    name: string;
    constructor(name: string) {
        this.name = name;
    }
    getName(){
        return `This language is ${this.name}`;
    }
}

class python extends language {
    ver:number
    constructor(ver:number) {
        super('Python');
        this.ver = ver;
    }

    getName() {
        return `This is language is Python`;
    }
    getVersion(): string {
        return `This is Python ${this.ver}`;
    }
}

let myPython = new python(3.7);
console.log(myPython.getName());
