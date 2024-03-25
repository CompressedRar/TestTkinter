navigation = document.getElementById("nav-bar");
activebar = document.getElementById("active-bar");

window.onscroll = () => {
    if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
        
        navigation.style.opacity = "0.7";
        activebar.style.opacity = "0.7";
      }
    else if (document.body.scrollTop < 350 || document.documentElement.scrollTop < 350){
        navigation.style.backgroundColor = "#0f1e29";
        navigation.style.opacity = "1";
        activebar.style.opacity = "1";
        activebar.style.backgroundColor = "#0f1e29";
    }
}

function active(element){
    document.getElementById("active-bar").children[0].style.borderRightStyle = "none";
    document.getElementById("active-bar").children[1].style.borderRightStyle = "none";
    document.getElementById("active-bar").children[2].style.borderRightStyle = "none";
    document.getElementById("active-bar").children[3].style.borderRightStyle = "none";
    console.log(element)
    element.style.borderWidth = "5px";
    element.style.borderRightStyle = "solid";
    element.style.borderColor = "#31CF0B;"
}