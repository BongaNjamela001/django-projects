////circle image variables in themeselector extracted by id
// var comp = document.getElementById("compcircle");
// var elec = document.getElementById("eleccircle");
// var math = document.getElementById("mathcircle");
// var phys = document.getElementById("physcirle");
// var git = document.getElementById("gitcircle");
//selector text extracted by id
var defaulttext = document.getElementById("defaulttext");
var phystext = document.getElementById("phystext");
var comptext = document.getElementById("comptext");
var gittext = document.getElementById("gittext");
var mathtext = document.getElementById("mathtext");
var electext = document.getElementById("electext");

//on mouse out
function defaultText() {
    comptext.style.display = "none";
    gittext.style.display = "none";
    mathtext.style.display = "none";
    phystext.style.display = "none";
    electext.style.display = "none";
    defaulttext.style.display = "inline";
}

//function changes text over portfolio selecto based on the circle
//that is hovered over
function compTextOnHover(){
    //set text to compeng
    defaulttext.style.display = "none";
    1000;
    comptext.style.display = "inline";
}

function gitTextOnHover(){
    //set text to git
    defaulttext.style.display = "none";
    gittext.style.display = "inline";
}

function elecTextOnHover(){
    //set text to eleceng
    defaulttext.style.display = "none";
    electext.style.display = "inline";
}

function mathTextOnHover(){
    //set text to eleceng
    defaulttext.style.display = "none";
    mathtext.style.display = "inline";
}

function physTextOnHover(){
    //set text to eleceng
    defaulttext.style.display = "none";
    phystext.style.display = "inline";
}