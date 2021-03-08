<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <title>Листинг 5</title>
</head>
<body>
    <div class="container mt-4">
        <a href="../index.php"
           class="btn btn-outline-secondary btn-lg btn-block mb-5">Назад</a>
        <?php
        const MINUTES = 60;
        $h = 3.5;
        echo 'Число минут в указанном значении(3.5) в часах = ' . ($h * MINUTES) . '<br>';
        echo 'Методичка пройдена на версии языка PHP ' . PHP_VERSION;
        ?>
    </div>
</body>
</html>

