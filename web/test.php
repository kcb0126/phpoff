<?php
	exec("python3 app.py");
	echo file_get_contents("output.html");