<?php
setcookie('user', $user['login'], time() - 24 * 60 * 60, '/');
header('location: /');
?>
