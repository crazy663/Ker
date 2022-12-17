<html>
<head>
    <title>App page</title>
</head>
<body>
    <h2>Парсинг подписок youtube канала</h2>
    <h3>Введите название канала:</h3>
    <?php
    if (isset($_POST['urlpath'])){
        $myCurl = curl_init();
    curl_setopt_array($myCurl, array(
        CURLOPT_URL => 'http://nginxserver/api/'.$_POST['urlpath'],
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_HEADER => false,
    ));
    $response = curl_exec($myCurl);
    $return= curl_exec($ch);
    curl_close($myCurl);

    echo "Ответ на Ваш запрос: ".$response;
    }
    ?>
    <form action="index.php" method="post">
    <label for="urlpath">Канал для парсинга подписок: </label>
    <input type="text" name="urlpath" id="urlpath" required>
    <input type="submit" value="RUN!">
</body>
</html>