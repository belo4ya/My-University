<?php
$login = filter_var(trim($_POST['login']), FILTER_SANITIZE_STRING);
$password = filter_var(trim($_POST['password']), FILTER_SANITIZE_STRING);

$password = md5($password.'ge0f4ps');
$mysql = new mysqli('localhost', 'root', 'root', 'register');

$result = $mysql -> query("SELECT * FROM `users` WHERE `login` = '$login' and `password` = '$password'");
$user = $result -> fetch_assoc();
if (!$user){
    $error = 'Такой пользователь не найден';
    require_once('error.php');
    exit();
}

setcookie('user', $user['login'], time() + 24 * 60 * 60, '/');
$mysql -> close();
header('location: /');
?>
