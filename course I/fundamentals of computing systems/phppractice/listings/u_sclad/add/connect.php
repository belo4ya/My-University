<?php
$sqlhost = 'localhost';
$sqluser = 'ca38672_practice';
$sqlpass = 'practice';
$db = 'ca38672_practice';
$connect = mysqli_connect($sqlhost, $sqluser, $sqlpass) or exit('MeSQL не доступен' . mysqli_error($connect));
mysqli_select_db($connect, $db) or exit('Нет соединения с базой данных' . mysqli_error($connect));
