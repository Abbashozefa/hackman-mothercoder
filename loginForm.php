<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <link rel="stylesheet" href="assets/css/login.css">
</head>

<body>
    <div class="container right-panel-active">
        <!-- Sign Up -->
        <div class="container__form container--signup">
            <form action="login.php" class="form" id="form1" method="post">
                <h2 class="form__title">Sign Up</h2>
                <input type="text" placeholder="User" class="input" />
                <input type="email" placeholder="Email" class="input" />
                <input type="password" placeholder="Password" class="input" />
                <button name="submit" type="submit" value="SUBMIT" class="btn">Sign Up</button>
            </form>
        </div>

        <!-- Sign In -->
        <div class="container__form container--signin">
            <!-- <form action="login.php" class="form" id="form2" method="post">
                <h2 class="form__title">Sign In</h2>
                <input type="email" placeholder="Email" class="input" name="email" />
                <input type="password" placeholder="Password" class="input" name="password" />
                <button name="submit" type="submit" value="SUBMIT" class="btn">Sign In</button>
            </form> -->
            <form action="login.php" method="post" style="
            background-color: var(--white);
            display: flex;
            align-items: center;
            justify-content: center;
            flex-direction: column;
            padding: 0 3rem; 
            height: 100%;
            text-align: center;">
                <center>
                    <h2 class="form__title">Sign In</h2>
                    <div class="mb-3">
                        <!-- <label for="email" class="form-label">Email address</label> -->
                        <input type="email" placeholder="email" class="form-control input" id="email" name="email"
                            aria-describedby=" emailHelp">
                    </div>
                    <div class="mb-3">
                        <!-- <label for="email" class="form-label">Email address</label> -->
                        <input type="text" placeholder="username" maxlength="10" class="form-control input"
                            id="username" name="username" aria-describedby=" emailHelp">
                    </div>
                    <div class="mb-3">
                        <!-- <label for="password" class="form-label">Password</label> -->
                        <input type="password" class=" form-control input" id="password" placeholder="password"
                            name="password">
                    </div>
                    <button type=" submit" class="btn btn-primary">SignIn</button>
                </center>
            </form>
        </div>

        <!-- Overlay -->
        <div class="container__overlay">
            <div class="overlay">
                <div class="overlay__panel overlay--left">
                    <button class="btn" id="signIn">Sign In</button>
                </div>
                <div class="overlay__panel overlay--right">
                    <button class="btn" id="signUp">Sign Up</button>
                </div>
            </div>
        </div>
    </div>
    <script src="login.js"></script>
</body>

</html>