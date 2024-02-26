document.addEventListener('DOMContentLoaded', function() {
    var toSigninButton = document.getElementById('to-signin-button');
    var toLoginButton = document.getElementById('to-login-button');
    var loginWrapper = document.getElementById('login-wrapper');
    var signinWrapper = document.getElementById('signin-wrapper');
    console.log(signinWrapper)

    loginWrapper.style.display = 'none';
    signinWrapper.style.display = 'block';

    // サインインボタンがクリックされたとき
    toSigninButton.addEventListener('click', function() {
        loginWrapper.style.display = 'none';
        signinWrapper.style.display = 'block';
    });

    // ログインボタンがクリックされたとき
    toLoginButton.addEventListener('click', function() {
        signinWrapper.style.display = 'none';
        loginWrapper.style.display = 'block';
    });


    
});
