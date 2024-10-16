<?php
show_source(__FILE__);
error_reporting(0);
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

$cmd = unserialize($_POST[$c]);
throw new Exception("Error");
