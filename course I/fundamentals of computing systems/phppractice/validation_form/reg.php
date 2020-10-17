<?php
$login = filter_var(trim($_POST['login']), FILTER_SANITIZE_STRING);
$name = filter_var(trim($_POST['name']), FILTER_SANITIZE_STRING);
$password = filter_var(trim($_POST['password']), FILTER_SANITIZE_STRING);
$repeat = filter_var(trim($_POST['repeat']), FILTER_SANITIZE_STRING);

if (mb_strlen($login) < 5 || mb_strlen($login) > 80)
{
    $error = "Недопустимый Логин '$login'. Длина Логина должна быть больше 5 символов, но меньше 80";
    require_once('error.php');
    exit();
} elseif (mb_strlen($name) < 2 || mb_strlen($login) > 80)
{
    $error = "Недопустимое Имя '$name'. Длина Имени должна быть больше 2 символов, но меньше 80";
    require_once('error.php');
    exit();
} elseif (mb_strlen($password) < 3 || mb_strlen($password) > 12)
{
    $error = "Длина Пароля должна быть больше 3 символов, но меньше 12";
    require_once('error.php');
    exit();
} elseif ($password != $repeat)
{
    $error = "Введенные пароли не совпадают";
    require_once('error.php');
    exit();
}

$mysql = new mysqli('localhost', 'ca38672_register', 'register', 'ca38672_register');
//$mysql = new mysqli('localhost', 'root', 'root', 'register');
$result = $mysql -> query("SELECT * FROM `users` WHERE `login` = '$login'");
$user = $result -> fetch_assoc();
if ($user){
    $error = "Логин '$login' занят. Используйте дргой Логин";
    require_once('error.php');
    exit();
}

$password = md5($password.'ge0f4ps');
$mysql -> query("INSERT INTO `users` (`login`, `password`, `name`) VALUES ('$login', '$password', '$name')");
$mysql -> close();
header('location: /');
?>
