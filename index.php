<?php
   echo exec('python counter.py');
   $eng_count = exec('python get_eng.py');
   $hits = exec('python hits.py');
   echo "Total Vistors: $hits ";
   $ip = $_SERVER['REMOTE_ADDR'];
   $ip_head = substr($ip, 0, 7);
   if ($ip_head == "158.130")
   	$eng_count = exec('python eng_count.py');
   echo "Visitors from Penn Engineering: $eng_count";

?>
