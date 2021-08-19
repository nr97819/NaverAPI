function input_Text(){
    document.getElementById("input1").value = "클라우드";
    document.getElementById("input2").value = "클라우드 보안";
}

function newClickEvent(){
    document.getElementById("loading-image").hidden = null;
    // document.getElementsByClassName("loading").style.position="fixed"
    // document.getElementsByClassName("loading").style.display="blocked"
}

function zoomIn(event) {
    event.target.style.transform = "scale(2.5)";
    event.target.style.zIndex = 1;
    event.target.style.transition = "all 0.4s";
}

function zoomOut(event) {
    event.target.style.transform = "scale(1)";
    event.target.style.zIndex = 0;
    event.target.style.transition = "all 0.4s";
}