<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="../css/style.css">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <title>Ошибка</title>
</head>
<body>
    <div class="container min-vh-100 min-vw-100 text-monospace error">
        <div class="container">
            <div class="row text-center align-items-center vh-100">
                <div class="col">
                    <div>Упс... ошибочка вышла:</div>
                    <div class="accent"><?php echo $error?></div>
                    <a href="../index.php" class="btn btn-outline-dark btn-lg text-uppercase">назад</a>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
