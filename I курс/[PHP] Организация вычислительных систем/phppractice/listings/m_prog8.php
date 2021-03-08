<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <title>Листинг 13</title>
</head>
<body>
    <div class="container mt-4">
        <a href="../index.php" class="btn btn-outline-secondary btn-lg btn-block mb-5">Назад</a>
        <?php
            echo 'Работает в паре с Листинг 12 (i_prog8.html)<hr>';
            if ($_GET['enter_system'] == 'OK')
            {
                echo 'Привет, ' . $_GET['name_of_user'] . '!';
                $f = fopen('files/names_prog8.txt', 'a+t') or exit('Файл не открывается');
                flock($f, 2);
                fputs($f, $_GET['name_of_user']);
                fputs($f, ' ');
                fputs($f, $_GET['variant']);
                fputs($f, '   ');
                flock($f, 3);
                fclose($f);
            }
            else
            {
                echo 'Ошибка';
            }
        ?>
    </div>
</body>
</html>
