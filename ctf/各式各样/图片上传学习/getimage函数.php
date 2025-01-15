<?php
$image_info = getimagesize("CTF\各式各样\图片上传学习\image.jpg");

if ($image_info !== false) {
    echo "Width: " . $image_info[0] . "px\n";
    echo "Height: " . $image_info[1] . "px\n";
    echo "Image type: " . $image_info[2] . "\n";
    echo "HTML attributes: " . $image_info[3] . "\n";
    echo "MIME type: " . $image_info['mime'];
} else {
    echo "Failed to get image size.";
}
?>