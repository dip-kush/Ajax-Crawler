<?php
	ob_start();
    session_start();
    if(!isset($_SESSION['Username'])){
         header("Location: login.php");
    }
    
    
?>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Member Area </title>
<style type="text/css">
 .success {
	border: 1px solid;
	margin: 0 auto;
	padding:10px 5px 10px 60px;
	background-repeat: no-repeat;
	background-position: 10px center;
     font-weight:bold;
     width:450px;
     color: #4F8A10;
	background-color: #DFF2BF;
	background-image:url('images/success.png');
     
}



</style>
</head>

<body>
<div class="success">Welcome , <?php echo $_SESSION['Username']	; ?></div>

<a href="profile.html"> profile</a>
<br />
<a href="hobby.html"> Hobby</a>
<br />
<fieldset>Feedback form 
<form method="get" action="feedback.php">

<input type="text" id="name" name="name" placeholder="name" /><br/>
<textarea cols="20" rows="4" name="fb" placeholder="feedback"> </textarea> <br/>
<input type="submit" value="feedback" />	
</form>


</form>

</fieldset>
</body>
</html>
