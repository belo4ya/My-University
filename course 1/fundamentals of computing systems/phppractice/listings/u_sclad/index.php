<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <title>Document</title>
</head>
<body>
    <div class="container mt-4">
        <a href="../../index.php"
           class="btn btn-outline-secondary btn-lg btn-block mb-5">Назад</a>
        <?php
            require_once('add/connect.php');
            $sql = 'SELECT name FROM users ORDER BY name';
            $result = mysqli_query($connect, $sql);
        ?>
        <form action="add/start.php" method="post">
            <label>
                <select name="z1">
                    <?php
                        while ($line=mysqli_fetch_row($result))
                        {
                            echo "<option value='" . $line[0] . "'>$line[0]";
                        }
                    ?>
                </select>
            </label><br><br>
            <span>Пароль:</span>
            <label>
                <input type="password" name="pass1">
            </label>
            <label>
                <input name="enterstart" style="font-size: 14pt; font-family: Tahoma, sans-serif"
                type="submit" value="Перейти к работе с базой">
            </label>
        </form>
    </div>
</body>
</html>
