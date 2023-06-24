<?php
session_start();
include('dbconn.php');
if (($_SERVER['REQUEST_METHOD'] == 'POST')) {
    $email = $_POST['email'];
    $clearTextPassword = $_POST['password'];
    $username = $_POST['username'];

    try {
        $user = $auth->getUserByEmail("$email");

        try {
            $signInResult = $auth->signInWithEmailAndPassword($email, $clearTextPassword);
            $idTokenString =  $signInResult->idToken();

            try {
                $verifiedIdToken = $auth->verifyIdToken($idTokenString);
                $uid = $verifiedIdToken->claims()->get('sub');

                
                $_SESSION['verified_user_id']=$uid;
                $_SESSION['idtokenstring']=$idTokenString;
                
                $_SESSION['status'] = " Logged-in Succesfully ";
                 header("location:http://127.0.0.1:5000?user=$username");
                 exit();
                 
            } catch (FailedToVerifyToken $e) {
                echo 'The token is invalid: ' . $e->getMessage();
            }



        } catch (Exception $e) {
            $_SESSION['status'] = " Wrong Password ";
            header("location:loginForm.php");
            exit();
        }


    } catch (\Kreait\Firebase\Exception\Auth\UserNotFound $e) {
        // echo $e->getMessage();

        $_SESSION['status'] = " invalid credentials ";
        header("location:loginForm.php");
        exit();
    }
} else {
    $_SESSION['status'] = "Not Allowed";
    header("location:loginForm.php");
    exit();
}
?>