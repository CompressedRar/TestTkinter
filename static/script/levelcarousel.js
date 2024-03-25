desc = [{
    "level": 1,
    "scope": "Hydrogen - Neon",
    "bg": "url('/static/Elements/23.Vanadium.png')"
},{
    "level": 2,
    "scope": "Sodium - Calcium",
    "bg": "url('/static/Elements/5.Boron.png')"
},{
    "level": 3,
    "scope": "Scandium - Zinc",
    "bg": "url('/static/Elements/13.Aluminium.png')"
},{
    "level": 4,
    "scope": "Gallium - Zirconium",
    "bg": "url('/static/Elements/26.Iron.png')"
},{
    "level": 5,
    "scope": "Niobium - Tin",
    "bg": "url('/static/Elements/34.Selenium.png')"
},{
    "level": 6,
    "scope": "Antimony - Neodymium",
    "bg": "url('/static/Elements/49.Indium.png')"
},{
    "level": 7,
    "scope": "Promethium - Ytterbium",
    "bg": "url('/static/Elements/69.Thulium.jpg')"
},{
    "level": 8,
    "scope": "Lutetium - Mercury",
    "bg": "url('/static/Elements/75.Rhenium.jpg')"
},{
    "level": 9,
    "scope": "Thallium - Thorium",
    "bg": "url('/static/Elements/92.Uranium.jpg')"
},{
    "level": 10,
    "scope": "Proctactinium - Fermium",
    "bg": "url('/static/Elements/106.Seaborgium.jpg')"
},{
    "level": 11,
    "scope": "Mendelevium - Darmstadtium",
    "bg": "url('/static/Elements/111.Roentgenium.jpg')"
},{
    "level": 12,
    "scope": "Roentgenium - Oganesson",
    "bg": "url('/static/Elements/102.Nobelium.jpg')"
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
    lvl.textContent = "Level " + desc[carouselpointer]["level"];
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