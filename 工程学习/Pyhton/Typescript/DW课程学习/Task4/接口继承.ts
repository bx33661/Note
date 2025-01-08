interface Preson {
    name: string
    age: number
    gender: '男' | '女'
}

interface Student extends Preson {
    grade: number
}

let student: Student = {
    name: '小明',
    age: 18,
    gender: '男',
    grade: 1
}

console.log(student) // { name: '小明



