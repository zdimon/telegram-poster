<?php 

function httpPost($url, $data)
{
    $curl = curl_init($url);
    curl_setopt($curl, CURLOPT_POST, true);
    curl_setopt($curl, CURLOPT_POSTFIELDS, http_build_query($data));
    curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
    $response = curl_exec($curl);
    curl_close($curl);
    return $response;
}

$data = ['secret'=>'123','message'=>'test message'];
$url = 'http://95.217.152.36:7777/notify/';
$res = httpPost($url,$data);
var_dump($res);

?>