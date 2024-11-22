<?php
$strings = [
    "0e215962017",
    "0e1284838308",
    "0e1137126905",
    "0e807097110",
    "0e730083352"
];

foreach ($strings as $string) {
    $md5_hash = md5($string);
    echo "MD5 hash of '$string' is: $md5_hash\n";
}
?>
