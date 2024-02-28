<?php
/* Car Class */
class Car {
    // Properties
    public $make;
    public $model;
    public $year;
    
    // Methods
    function __construct($make, $model, $year) {
    	$this->make = $make;
        $this->model = $model;
        $this->year = $year;
    }
    
    function set_make($make) {
        $this->make = $make;
    }
    function get_make() {
        return $this->make;
    }

    function set_model($model) {
        $this->model = $model;
    }
    function get_model() {
        return $this->model;
    }

    function set_year($year) {
        $this->year = $year;
    }
    function get_year() {
        return $this->year;
    }
    
    function description() {
        return $this->year.' '.$this->make.' '.$this->model;
    }
}
