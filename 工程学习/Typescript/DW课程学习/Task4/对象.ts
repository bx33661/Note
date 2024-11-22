let langauge_program = {
    name1:"cpp",
    name2:"java",
    name3:"python",
    name4:"javascript",
    name5:"typescript",
}
//console.log(langauge_program.name1);
//console.log(langauge_program.name2);
//console.log(langauge_program.name3);

function sayName(name: string) {
    return 'Hello, ' + name;
}
console.log(sayName(langauge_program.name3)); // Hello, typescript