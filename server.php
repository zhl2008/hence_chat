<?php
error_reporting(E_ALL);
date_default_timezone_set('Asia/shanghai');
header('Access-Control-Allow-Origin: *');
header('Content-Type:text/html;charset=utf-8');

if(isset($_GET['op'])){
    $op = $_GET["op"];
    if ( $op == "send" && isset($_REQUEST["data"]) ) {
	file_put_contents('now.txt',$_REQUEST["data"]."\n",FILE_APPEND);
    }
    elseif ( $op == "read"  && isset($_GET["seq"])){
	$line = $_GET["seq"];
	$file=fopen("now.txt","r");
	$result = "null";
	$i = 1;
	if($file){
	    while(!feof($file))
	    {	
		$tmp = fgets($file);
		if($line == $i && $tmp){;
		    $result = $tmp;
		    break;
		}
		$i++;
	    }
	}
	echo $result;
	fclose($file);
    }
}
?>
