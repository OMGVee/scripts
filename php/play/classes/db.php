<?php
require_once("class.log.php");
class Db
{
	function connect($host,$user,$pass)
	{
		if (!mysql_connect($host,$user,$pass)) die ("");
	}
}
?>
