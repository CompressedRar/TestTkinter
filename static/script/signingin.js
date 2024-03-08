console.log("Hehe");    

toggleLogin = document.getElementById("login-account_label");
toggleSignin = document.getElementById("create-account__label");

signform = document.getElementById("signin-form");
loginform = document.getElementById("login-form");

isSignInOpen = false;
loginform.style.zIndex = "1";

function loginBringToFront(){
    loginform.style.zIndex = "1";
}
function loginSendToBack(){
    loginform.style.zIndex = "0";
}

function signinBringToFront(){
    signform.style.zIndex = "1";
}
function signinSendToBack(){
    signform.style.zIndex = "0";
}


toggleSignin.addEventListener("click", ()=>{
    loginform.style.opacity = "0";
    signform.style.opacity = "1";
    isSignInOpen = true;
});

loginform.addEventListener("transitionend", ()=>{
    if(isSignInOpen){
        loginSendToBack();
    }
    else {
        loginBringToFront();
    }
});

toggleLogin.addEventListener("click", ()=>{
    signform.style.opacity = "0";
    loginform.style.opacity = "1";
    
    isSignInOpen = false;
});