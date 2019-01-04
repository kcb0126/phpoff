<?php
	exec("python app.py");
	echo file_get_contents("output.html");