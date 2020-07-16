<?php

/* Author: sangco */
function inject_check($sql_str) {
	//$check = preg_match('/select|insert|update|delete|\'|\/\*|\*|\.\.\/|\.\/|union|into|load_file|outfile/', $sql_str, $matches, PREG_OFFSET_CAPTURE);
	$check = preg_match('/select|insert|update|delete|into|load_file|outfile/', $sql_str, $matches, PREG_OFFSET_CAPTURE);
	
	if ($check > 0) {
		echo 'ban hacker  by q120018425';
		exit ;

	} else {
		
			
		return $sql_str;
	}

}


foreach ($_GET as $get_key => $Get_var) {
	inject_check($Get_var);
}
foreach ($_POST as $post_key => $post_var) {
	inject_check($post_var);
}

foreach ($_COOKIE as $Cook_key => $Cook_var) {
	inject_check($Cook_var);
}





?>