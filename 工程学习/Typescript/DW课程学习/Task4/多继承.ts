//多继承
interface Preson_name {
    name: string
}

interface Preson_age {
    age: number
}

interface Preason extends Preson_age,Preson_name{
    gender: '男' | '女'
}

let man: Preason = {
    name: '田山',
    age: 18,
    gender: '男'
}

console.log(man)