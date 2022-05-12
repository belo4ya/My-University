<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <title>Листинг 17</title>
</head>
<body>
    <div class="container mt-4">
        <a href="../index.php" class="btn btn-outline-secondary btn-lg btn-block mb-5">Назад</a>
        <?php
            echo 'Работает в паре с Листинг 16 (p_prog10.html)<hr>';
            if (isset($_POST['okb']))
            {
                echo 'Получатель - ' . $_POST['person'];
                $komu = 'best_email@galaxy.com';
                $tema = 'Вопрос от ' . $_POST['person'] . ' ' . $_POST['email'];
                $text_pisma = $_POST['q'];
                $z = mail($komu, $tema, $text_pisma);
                echo '<br> Письмо отправлено!(нет)';
            }
            else
            {
                echo 'Ошибка';
            }
        ?>
    </div>
</body>
</html>
