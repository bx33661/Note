<?php
file_put_contents("example.txt", "nihaoshijie!");
$content  =file_get_contents("example.txt");
echo $content;
?>