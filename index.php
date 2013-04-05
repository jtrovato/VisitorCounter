<?php
   echo exec('python hello.py');
   exec('python hits.py', $hits);
   echo $hits;
?>
