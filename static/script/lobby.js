navigation = document.getElementById("nav-bar");
activebar = document.getElementById("active-bar");

window.onscroll = () => {
    if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
        navigation.style.backgroundColor = "rgba(67,67,120,0.3)";
        navigation.style.opacity = "0.3";
        activebar.style.opacity = "0.3";
        activebar.style.backgroundColor = "rgba(67,67,120,0.3)";
      }
    else if (document.body.scrollTop < 350 || document.documentElement.scrollTop < 350){
        navigation.style.backgroundColor = "#164464";
        navigation.style.opacity = "1";
        activebar.style.opacity = "1";
        activebar.style.backgroundColor = "#164464";
    }
}

function active(element){
    document.getElementById("active-bar").children[0].style.borderTopStyle = "none";
    document.getElementById("active-bar").children[1].style.borderTopStyle = "none";
    document.getElementById("active-bar").children[2].style.borderTopStyle = "none";
    document.getElementById("active-bar").children[3].style.borderTopStyle = "none";
    console.log(element)
    element.style.borderWidth = "5px";
    element.style.borderTopStyle = "solid";
    element.style.borderColor = "#31CF0B;"
}