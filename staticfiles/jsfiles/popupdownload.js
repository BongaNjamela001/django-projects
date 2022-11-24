// function openForm() {
//     var popup = document.getElementById("popup"); 
//     if (popup.style.display === "none") {
//         popup.style.display = "block";
//     }
//     else {
//         popup.style.display = "none";
//     }
// }

function openForm() {
    var popup = document.getElementById("popup"); 
    popup.classList.toggle("show")
}

function closeForm() {
    var popup = document.getElementById("popup");
    if (popup.style.display === "block") {
        popup.style.display = "none";
    }
    else {
        popup.style.display = "none";
    }
}