<?php
$sqlhost = 'localhost';
$sqluser = 'root';
$sqlpass = 'root';
$db = 'Firma';
$connect = mysqli_connect($sqlhost, $sqluser, $sqlpass) or exit('MeSQL не доступен' . mysqli_error($connect));
mysqli_select_db($connect, $db) or exit('Нет соединения с базой данных' . mysqli_error($connect));
