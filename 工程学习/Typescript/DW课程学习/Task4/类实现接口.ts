//类实现接口
interface Game{
    name:string;
    player:string;
    play():void;
}

class Basketball implements Game{
    name = 'Basketball';
    player = '5';
    play(){
        console.log(`I love ${this.name}, ${this.player} players in a team.`);
    }
}

let basketball = new Basketball();
basketball.play(); // I love Basketball, 5 players in a team.
console.log(basketball.name); // Basketball
console.log(basketball.player); // 5