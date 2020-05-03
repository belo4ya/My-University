<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <title>Листинг 19</title>
</head>
<body>
    <div class="container mt-4">
        <a href="../index.php" class="btn btn-outline-secondary btn-lg btn-block mb-5">Назад</a>
        <form action="t_add_message.php" method="post">
            <span>Имя:</span><br>
            <label>
                <input type="text" name="name_of_quest">
            </label><br><br>
            <span>Сообщение:</span><br>
            <label>
                <textarea name="message_of_quest" cols=10 rows=5></textarea>
            </label><br>
            <label>
                <input type="submit" name="okbutton" value="OK">
            </label>
        </form>
        <?php
            $f = fopen('files/gost.txt', 'rt') or exit('Не могу открыть файл');
            while (!feof($f))
            {
                $data = fgets($f);
                echo '<small>Имя:</small>' . $data . '<br>';
                $data = fgets($f);
                echo '<small>Сообщение:</small>' . $data . '<br>';
                echo '<hr>';
            }
            fclose($f)
        ?>
    </div>
</body>
</html>
