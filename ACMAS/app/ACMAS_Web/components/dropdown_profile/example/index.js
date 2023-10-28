function rotate() {
    document.getElementById("diameter").classList.add("hover");
    document.getElementById("X").classList.add("opacity-100");
    document.getElementById("X").classList.add("visible");
    document.getElementById("X").classList.remove("opacity-0");
    document.getElementById("X").classList.remove("invisible");
    document.getElementById("Y").classList.add("opacity-100");
    document.getElementById("Y").classList.add("visible");
    document.getElementById("Y").classList.remove("opacity-0");
    document.getElementById("Y").classList.remove("invisible");
    document.getElementById("Z").classList.add("opacity-100");
    document.getElementById("Z").classList.add("visible");
    document.getElementById("Z").classList.remove("opacity-0");
    document.getElementById("Z").classList.remove("invisible");

    document.getElementById("hover-zone").classList.add("visible");
    document.getElementById("hover-zone").classList.remove("invisible");
}

function reset() {
    document.getElementById("diameter").classList.remove("hover");
    document.getElementById("X").classList.add("opacity-0");
    document.getElementById("X").classList.remove("opacity-100");

    document.getElementById("Y").classList.add("opacity-0");
    document.getElementById("Y").classList.remove("opacity-100");

    document.getElementById("Z").classList.add("opacity-0");
    document.getElementById("Z").classList.remove("opacity-100");
}

document.getElementById("X").addEventListener("transitionend", function() {
    if(this.classList.contains("opacity-0")) {
        document.getElementById("X").classList.add("invisible");
        document.getElementById("X").classList.remove("visible");
        document.getElementById("Y").classList.add("invisible");
        document.getElementById("Y").classList.remove("visible");
        document.getElementById("Z").classList.add("invisible");
        document.getElementById("Z").classList.remove("visible");
        document.getElementById("hover-zone").classList.add("invisible");
        document.getElementById("hover-zone").classList.remove("visible");
    }
});