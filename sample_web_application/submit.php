<?php



include ('database_connection.php');

$name = $_GET['name'];

$query = "insert into submit(name) values('$name')";

 $result_check_credentials = mysqli_query($dbc, $query);
        if(!$result_check_credentials){//If the QUery Failed 
            echo 'Query Failed ';
        }
	else{
	    echo "<title>form2</title>  <p>Query Submitted</p>";
           // echo "<a href='login'>login</a>";
	}

?>
