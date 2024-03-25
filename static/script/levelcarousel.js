desc = [{
    "level": 1,
    "scope": "Hydrogen - Neon",
    "bg": "url('/static/Elements/23.Vanadium.png')"
},{
    "level": 2,
    "scope": "Sodium - Calcium",
    "bg": "url('/static/Elements/12.Magnesium.jpg')"
},{
    "level": 3,
    "scope": "Scandium - Zinc",
    "bg": "url('/static/Elements/27.Cobalt.png')"
},{
    "level": 4,
    "scope": "Gallium - Zirconium",
    "bg": "url('/static/Elements/24.Chromium.png')"
},{
    "level": 5,
    "scope": "Niobium - Tin",
    "bg": "url('/static/Elements/31.Gallium.png')"
},{
    "level": 6,
    "scope": "Antimony - Neodymium",
    "bg": "url('/static/Elements/39.Yttrium.png')"
},{
    "level": 7,
    "scope": "Promethium - Ytterbium",
    "bg": "url('/static/Elements/52.Tellurium.jpg')"
},{
    "level": 8,
    "scope": "Lutetium - Mercury",
    "bg": "url('/static/Elements/62.Samarium.jpg')"
},{
    "level": 9,
    "scope": "Thallium - Thorium",
    "bg": "url('/static/Elements/78.Platinum.jpg')"
},{
    "level": 10,
    "scope": "Proctactinium - Fermium",
    "bg": "url('/static/Elements/102.Nobelium.jpg')"
},{
    "level": 11,
    "scope": "Mendelevium - Darmstadtium",
    "bg": "url('/static/Elements/109.Meitnerium.jpg')"
},{
    "level": 12,
    "scope": "Roentgenium - Oganesson",
    "bg": "url('/static/Elements/118.Oganesson.png')"
}];

let carouselpointer = 0;
carousel = document.getElementsByClassName("carousel")[0];
leftbutton = document.getElementById("leftbutton");
rightbutton = document.getElementById("rightbutton");


let lvl = document.getElementById("level");
let scope = document.getElementById("scope");

carousel.style.backgroundImage = desc[carouselpointer]["bg"];
lvl.textContent = "Level" + desc[carouselpointer]["level"];
scope.textContent = desc[carouselpointer]["scope"];

rightbutton.addEventListener("click", ()=>{
    if (carouselpointer < 11){
        carouselpointer += 1;
    }
    else {
        carouselpointer = 0;
    }
    
    carousel.style.backgroundImage = desc[carouselpointer]["bg"];
    lvl.textContent = "Level" + desc[carouselpointer]["level"];
    scope.textContent = desc[carouselpointer]["scope"];
    
});

leftbutton.addEventListener("click", ()=>{
    if (carouselpointer > 0){
        carouselpointer -= 1;
    }
    else {
        carouselpointer = 11;
    }
    carousel.style.backgroundImage = desc[carouselpointer]["bg"];
    lvl.textContent = "Level" + desc[carouselpointer]["level"];
    scope.textContent = desc[carouselpointer]["scope"];
    
});
console.log(desc[0][1]);