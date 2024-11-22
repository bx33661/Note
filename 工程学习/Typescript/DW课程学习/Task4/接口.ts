//接口
interface namel{
    [index:number]:string
}

let list2:namel = ['Python','JavaScript','TypeScript']


interface  name2{
    [index:string]:string
}
let list3:name2 = {
    'name':'Python',
    'name2':'JavaScript',
    'name3':'TypeScript'
}
console.log(list3['name'])