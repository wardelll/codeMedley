<?php
spl_autoload_register(function ($class) {
    include 'classes/'.$class.'.php';
});

?>
<!DOCTYPE html>
<html lang="en">
<meta charset="UTF-8">
<title>PHP Code Sample</title>
<meta name="viewport" content="width=device-width,initial-scale=1">
<link rel="stylesheet" href="/css/styles.css">
<script src=""></script>
<body>
<div id="content">

    <div>
        <?php 
        $myGreeting = new Greeting();
        echo $myGreeting->greet();
        ?>
    </div>

    <div>
        <?php 
        $greetBob = new Greeting("Hola","Bob");
        echo $greetBob->greet();
        ?>
    </div>

    <div>
    <?php
        $corvette = new Car("Chevy", "Corvette", "2024"); 
        echo $corvette->description(); 
    ?>
    </div>

    <div>
    <?php
        $crv = new Car("Honda", "CR-V", "2023"); 
        echo $crv->description(); 
    ?>
    </div>

    <div>
        <?php
        function doubleUp($keyValue){
            if(is_numeric($keyValue)){
                return $keyValue * 2;
            }else{
                return "sorry not a number ";
            }
        }

        $myArray = [2,3,'A',3.5];
        print_r($myArray);
        print '<br />Double Up!<br />';
        print_r(array_map("doubleUp",$myArray));
        ?>
    </div>

</div>
</body>
</html>
