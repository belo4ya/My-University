<?php
    if (isset($_POST['okbutton']))
    {
        if ($_POST['name_of_quest'] == '')
        {
            exit('Введите имя <a href="s_questbook.php">Назад!</a>>');
        }
        if ($_POST['message_of_quest'] == '')
        {
            exit('Введите сообщение <a href="s_questbook.php">Назад!</a>>');
        }
        $f = fopen('files/gost.txt', 'at') or exit('Не могу открыть файл');
        flock($f, 2);
        fputs($f, $_POST['name_of_quest'] . "\n");
        fputs($f, $_POST['message_of_quest'] . "\n");
        flock($f, 3);
        fclose($f);
    }
    header('location:s_questbook.php');
