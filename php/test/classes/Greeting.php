<?php
/* Car Class */
class Greeting {
    // Properties
    public $greetingTxt;
    public $userName;

    // Methods
    function __construct($greetingTxt = "Hello",$userName="World"){
        $this->userName = $userName;
        $this->greetingTxt = $greetingTxt;
    }

    function greet() {
        return $this->greetingTxt." ".$this->userName."!";
    }

}