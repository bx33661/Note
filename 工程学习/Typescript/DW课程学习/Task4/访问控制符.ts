class Phone {
    public region: string;
    private name: string;
    private price: number;
    constructor(name: string, price: number,region: string){
        this.region = region;
        this.name = name;
        this.price = price;
    }
    public getName(): string {
        return this.name;
    }
    public getPrice(): number {
        return this.price;
    }
}
let phone = new Phone('Huawei Meta 70',6999, 'China');
console.log(phone.getName());
console.log(phone.getPrice());

console.log(phone.region);
//console.log(phone.name);
//console.log(phone.price);
