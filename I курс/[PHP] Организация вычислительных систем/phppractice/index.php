<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <link rel="stylesheet" href="css/main.css">
    <title>Главная</title>
</head>
<body>
    <div class="container-fluid text-monospace">
        <div class="container justify-content-center">
            <div class="row text-center align-items-center" style="height: 380px">
                <div class="col px-md-5">
                    <h1>Разработка информационных систем для
                        сети интернет с использованием РНР и MySQL</h1>
                </div>
            </div>
            <div class="row text-center align-items-center">
                <?php if (!$_COOKIE['user']): ?> <!-- Форма регистрации, если не установлен cookie -->
                <div class="col-md-3">
                    <br><h2>Работу<br>выполнил<br><b>Ковалев<br>Алексей</b><br>студент<br>группы<br><b>ПИ19-3</b></h2>
                </div>
                <div class="col-md-6 my-5">
                    <h2><span class="accent">Вход на сайт</span></h2>
                    <form action="validation_form/auth.php" method="post">
                        <label>
                            <input type="text" class="form-control form-control-lg mt-4" name="login"
                                   id="login" placeholder="Введите Логин"><br>
                            <input type="password" class="form-control form-control-lg" name="password"
                                   id="password" placeholder="Введите Пароль"><br>
                            <button class="btn btn-outline-success btn-lg btn-block mt-2" type="submit">Войти</button>
                        </label>
                    </form>
                </div>
                <div class="col-md-3">
                    <h2><b>Быстрая регистрация</b></h2>
                    <form action="validation_form/reg.php" method="post">
                        <label>
                            <input type="text" class="form-control form-control mt-2" name="login"
                                   id="login" placeholder="Введите Логин"><br>
                            <input type="text" class="form-control" name="name"
                                   id="name" placeholder="Введите Имя"><br>
                            <input type="password" class="form-control" name="password"
                                   id="password" placeholder="Введите Пароль"><br>
                            <input type="password" class="form-control" name="repeat"
                                   id="repeat" placeholder="Повторите Пароль"><br>
                            <button class="btn btn-outline-warning btn btn-block" type="submit">Создать аккаунт</button>
                        </label>
                    </form>
                </div>
                <?php else:?> <!-- Иначе, контент -->
                    <div class="container text-center">
                        <a href="validation_form/exit.php"
                           class="btn btn-outline-warning btn-lg first-m mb-4">Выйти</a>
                        <a href="https://github.com/belo4ya" target="_blank"
                           class="btn btn-outline-success btn-lg first-m mb-4">Исходники</a>
                        <?php require_once("menu_bar.php");?>
                    </div>
                <?php endif;?>
            </div>
        </div>
    </div>
</body>
</html>
