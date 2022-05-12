<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <link rel="stylesheet" href="../css/main.css">
    <title>Ошибка</title>
</head>
<body>
    <div class="container-fluid min-vh-100 justify-content-center text-monospace error">
        <div class="container">
            <div class="row text-center align-items-center">
                <div class="col mt-5">
                    <div class="mt-5">Упс... ошибочка вышла:</div>
                    <div class="sub-error mt-5 w-75 mx-auto"><?php echo $error?></div>
                    <a href="../index.php" class="btn btn-outline-dark btn-lg text-uppercase my-5">назад</a>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
