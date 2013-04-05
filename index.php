<?php
   echo exec('python counter.py');
   $hits = exec('python hits.py');
   echo $hits;
?>
