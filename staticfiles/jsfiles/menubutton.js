/*
 * Script title: Menu Button Functions
 * Purpose: For handling display of menu button
 * @author: Bonga Njamela
 * @version: 06 December 2022
 */

//-----------------------------Global variables------------------------
//viewport dimensions
var veiwportH = window.innerHeight;
var viewportW = window.innerWidth;

//menu attributes
var mediummenu =  document.getElementById("medmenu");
var largemenu = document.getElementById("larmenu");
var menubutton = document.getElementById("menubutton");
var menuhover = document.getElementById("menubuttonhover");

/*
 * <p> 
 *     For choosing between menus based on viewport width when menu icon
 *     is clicked
 * </p> 
 */
function showMenu() {
    getViewportDims();
    if (viewportW < 1201) {
        menubutton.style.display = "none";
        mediummenu.style.display = "inline-block";
        largemenu.style.display = "none";
        menuhover.style.display = "none";
        // console.log(viewportW);
    }
    else {
        mediummenu.style.display = "none";
        largemenu.style.display = "inline-block";
        menubutton.style.display = "none";
        menuhover.style.display = "inline";
        // console.log(viewportW);
    }
}

/*
 * <p> For hiding menu when menu icon is clicked</p> 
 */
function hideMediumMenu() {
    if (viewportW < 1201) {
        mediummenu.style.display = "none";
        largemenu.style.display = "none";
        menubutton.style.display = "inline";
        menuhover.style.display = "none";
    }
    else {
        mediummenu.style.display = "none";
        largemenu.style.display = "none";
        menubutton.style.display = "inline";
        menuhover.style.display = "none";
    }
}

/*
 * <p> Get the viewport height and width </p> 
 */
function getViewportDims() {
    //viewport dimensions
    veiwportH = window.innerHeight;
    viewportW = window.innerWidth;
}

/* 
 * Function for hiding the menu button when user clicks outside 
 * the menu button div
 */
document.addEventListener('click', function handleClickOutsideBox(event) {
    if (!menubutton.contains(event.target)) {
      largemenu.style.display = "none";
      mediummenu.style.display = "none";
      menubutton.style.display = "inline";
      menuhover.style.display = "none";
    }
});