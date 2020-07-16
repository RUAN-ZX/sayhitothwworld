<?php

class mydb {
	var $dbhost;
	var $dbPort;
	var $dbuser;
	var $dbPassWord;
	var $dbname;
	var $charset;
	var $conn;
	public function __construct($host, $port, $username, $pwd, $dbname, $charset = "uft8") {
		$this -> dbhost = $host;
		$this -> dbPort = $port;
		$this -> dbuser = $username;
		$this -> dbPassWord = $pwd;
		$this -> dbname = $dbname;
		$this -> charset = $charset;
		self::conncent();

	}

	public function __destruct() {
		mysqli_close($this -> conn);

	}

	public function conncent() {
		$this -> conn = mysqli_connect($this -> dbhost, $this -> dbuser, $this -> dbPassWord, $this -> dbname, $this -> dbPort);
		if (!$this -> conn) {
			die(mysqli_errno($this -> conn));

		}
		//mysqli_select_db($this->conn, $this -> dbname);
		mysqli_query($this -> conn, 'SET NAMES ' . $this -> charset);

	}

	public function query($query) {
		$sql = $query;
		$query = mysqli_query($this -> conn, $sql);
		if ($query) {
			return $query;
		} else {
			self::log(mysqli_error($this -> conn) . $sql);
			die(mysqli_error($this -> conn) . $sql);
		}

		//return $query ? $query : die(mysql_error() . $sql);
	}

	public function get($query) {
		return mysqli_fetch_array($query);

	}
	//直接执行sql语句
	public function Num_row($query) {
		return mysqli_num_rows($this -> query($query));

	}

	public function Fomat($sql) {
		return mysqli_real_escape_string($this -> conn, $sql);
	}

	function log($logthis) {
		file_put_contents('logfile.log', date("Y-m-d H:i:s") . " " . $logthis . PHP_EOL, FILE_APPEND | LOCK_EX);
	}

}

?>