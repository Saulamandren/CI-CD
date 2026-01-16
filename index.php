<?php
session_start();

if (!isset($_SESSION['username'])) {
    header("Location: login.php");
    exit;
}
?>

<h1>Login Berhasil</h1>
<p>Selamat datang, <?= $_SESSION['username']; ?></p>
<a href="logout.php">Logout</a>
