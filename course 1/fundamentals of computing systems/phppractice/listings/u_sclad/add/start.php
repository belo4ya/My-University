<?php
if (isset($_POST['enterstart']))
{
    require_once ('connect.php');
    $par = md5($_POST['pass1']);
    $sql = "SELECT name, pass FROM users WHERE name='" . $_POST['z1'] . "' and pass='" . $par . "'";
    $res = mysqli_query($connect, $sql);
    if (!mysqli_num_rows($res))
    {
        exit('Неверный пароль <br><a href="../index.php"><br>Вернуться на главную страницу</a>');
    } else
    {
        echo 'Авторизация прошла успешно!!!';
        echo "<form action='pr.php' method='post'>";
        echo "<input name='add1' type='submit' value='Перейти к работе'>";
        echo "</form>";
    }
}
else
{
    echo "<a href='../index.php'>Вернуться на главную страницу</a>";
}