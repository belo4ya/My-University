<!doctype html>
<html lang="en" xmlns="http://www.w3.org/1999/html">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <?php
        require_once ('connect.php');
        if (isset($_POST['enterNew']))
        {
            $sqlScl = 'SELECT id, naz FROM Scladi WHERE naz="' . $_POST['SclNewTovar'] . '"';
            $dataScl = mysqli_query($connect, $sqlScl);
            $lineScl = mysqli_fetch_row($dataScl);
            $zx = $_POST['NewCol'];
            $sqlNewTov = 'INSERT INTO Tovar SET tovar="' .
                $_POST['NewTovar'] . '", idScl=' . $lineScl[0] .
                ', Col=' . $zx;
            mysqli_query($connect, $sqlNewTov) or exit(mysqli_error($connect));
        }
        $sql = 'SELECT tovar, idScl, Col FROM Tovar ORDER BY tovar';
        $data = mysqli_query($connect, $sql);
    ?>
    <font style="font-size: 16px">Имеющиеся позиции товаров:</font>
    <table border=1>
        <?php
            while ($line=mysqli_fetch_row($data)) // Тут ошибка
            {
        ?>
        <tr><td>
        <?php
            echo $line[0];
        ?>
        </td><td>
        <?php
            $sq12 = 'SELECT id, naz FROM Scladi WHERE id=' . $line[1];
            $data2 = mysqli_query($connect, $sq12);
            $line2 = mysqli_fetch_row($data2);
            echo $line2[1];
        ?>
        </td><td>
        <?php
            echo $line[2];
        ?>
        </td></tr>
        <?php
            }
        ?>
    </table>
    <div style="position: absolute; top: 5px; left: 500px">
        <font size="+2">Форма ввода новых товаров</font>
        <form method="post" action="">
            <font style="font-size: 16pt"><br>Название нового товара:</font>
            <label>
                <input type="text" name="NewTovar" value="">
            </label><br><br>
            <?php
                $sql3 = 'SELECT id, naz FROM Scladi';
                $result3 = mysqli_query($connect, $sql3);
                echo 'Склад:<select name="SclNewTovar">';
                while ($line3 = mysqli_fetch_row($result3))
                {
                    echo "<option value='>" . $line3[1] . "'>$line3[1]";
                }
            ?>
            </select><br><br>
            Количество:<input type="text" name="NewCol" value=""><br>
            <br><br><br>
            <input name="enterNew" type="submit" value="Ввести товар">
        </form>
        <a href="../index.php">Вернуться на главную страницу</a>
    </div>
</body>
</html>
