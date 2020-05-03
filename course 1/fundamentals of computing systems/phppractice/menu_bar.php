<?php
$files = array_slice(scandir('listings'), 2);
unset($files[6]);
sort($files);
$links = array();
for ($i = 0; $i < count($files)-1; $i++)
{
    $number = $i + 1;
    $name = "<h5 class='card-title'>Листинг $number<h5>" . "<h6 class='card-subtitle text-muted'>($files[$i])</h6>";
    $href = "/listings/$files[$i]";
    $link = "<div class='col card mx-5 my-4'><div class='card-body px-0'><a class='card-link' href='$href'>" . $name . '</a></div></div>';
    array_push($links, $link);
}
array_push($links, "<div class='col card mx-5 my-4'><div class='card-body'><a class='card-link' href='/listings/$files[$i]'>" .
    "<h5 class='card-title'>'Склады'(БД)</h5>" .
    "<h6 class='card-subtitle text-muted'>($files[$i])</h6></a></div></div>");

$tmp = '';
for ($i = 0; $i < count($links); $i++)
{
    if ($i % 3 == 0) {
        $tmp = $tmp .'<div class="row">'. $links[$i];
    } elseif ($i % 3 == 1)
    {
        $tmp = $tmp . $links[$i];
    } else
    {
        $tmp = $tmp . $links[$i] . '</div>';
    }
}

echo $tmp;
