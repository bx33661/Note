<?php
$flaaaag = "successful demo";
class happy{
    public $num;
    function __construct($num)
    {
        $this->$num = $num;
    }
    function go(){
        echo "let's go!";
    }
    function __destruct()
    {
        global $flaaaag;
        echo $flaaaag;
    }
}


$a = array(new happy(1),0);
echo serialize($a);
