var span = document.getElementById('projectTitle');
var zipurl = "../portfolio/Advanced_Differential_Equations.zip"
var tarurl = "../portfolio/Advanced_Differential_Equations.tar.gz"
var popup = document.getElementById("popup");

function openPopUp(name, zipproj, tarproj) {
    // toggle the display of the popup when a project name is clicked
    createTarLink(tarproj);
    createZipLink(zipproj);

    if (popup.style.display === "none") {
            span.innerText = name;
            popup.style.display = "block";
    }
    else {
            popup.style.display = "none";
    }
}

function closePopUp() {
    // toggle the display of the popup when a project name is clicked
    var popup = document.getElementById("popup");
    if (popup.style.display === "block") {
        popup.style.display = "none";
    }
}

function createZipLink(staticurl) {
    zipurl = "/staticfiles/"+staticurl;
}

function createTarLink(staticurl) {
    tarurl = "/staticfiles/"+staticurl;
}

function downloadZip() {
    var downloadzip = document.getElementById("downloadzip");//zip <a> in projectpopup.html
    // var saveas = createZip(span.innerText);
    downloadzip.href = zipurl;
}

function downloadTar() {
    // var saveas = createTar(span.innerText);
    var downloadtar = document.getElementById("downloadtar");//zip <a> in projectpopup.html
    downloadtar.href = tarurl;
}

/* 
 * Function for hiding the popup button when user clicks outside 
 * the menu button div
 */
document.addEventListener('click', function handleClickOutsideBox(event) {
    if (!popup.contains(event.target)) {
        if (!(popup.style.display === "block")) {
            popup.style.display = "none";
        }
        else {
            popup.style.display = "block";
        }
    } 
});