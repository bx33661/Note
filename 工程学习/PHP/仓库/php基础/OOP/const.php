<?php
class Fruit{
    const WELCOME_MESSAGE = "hello,welcome to my world";
    public $first;
    public $second;
    public function __construct($first,$second)
    {
        $this->first = $first;
        $this->second = $second;
    }

    public function get_hello()
    {
        //return self::WELCOME_MESSAGE;
        return Fruit::WELCOME_MESSAGE;
    }
}

$a = new Fruit("apple","banana");
echo $a->second."     ".$a->first;
echo Fruit::WELCOME_MESSAGE;
