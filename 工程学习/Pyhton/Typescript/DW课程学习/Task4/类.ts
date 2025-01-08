//类
class Python {
    //类的属性
    version: number;
    //类的方法
    constructor(version: number) {
        this.version = version;
    }
    //类的方法
    getVersion() {
        console.log('Python' + this.version);
    }
}

let py = new Python(3.8);
py.getVersion();
