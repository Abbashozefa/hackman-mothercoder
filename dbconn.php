<?php

require __DIR__ . '/vendor/autoload.php';

use Kreait\Firebase\Factory;
use Kreait\Firebase\Contract\Auth;


$factory = (new Factory)
    ->withServiceAccount('wakey-wakey-a8b54-firebase-adminsdk-sopjz-d20335b372.json')
    ->withDatabaseUri('https://wakey-wakey-a8b54-default-rtdb.firebaseio.com/');

$database = $factory->createDatabase();
$auth = $factory->createAuth();
?>