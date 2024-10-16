<?php
if ((string)$_POST['param1'] !== (string)$_POST['param2'] && md5($_POST['param1']) === md5($_POST['param2'])) {
    die("success!");
}
?>
