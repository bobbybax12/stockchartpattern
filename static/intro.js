
function hmmmm(page) {
    // select h1
    $("h1").text(page[1]);
    // select the p element
    $("p").text(page[2]);
    // select hmmmm div and add image from page[3]
    let image = `<img src="${page[3]}" style="width: 500px; height: auto;">`
    $("#hm").append(image);
}



$(document).ready(function() {
    hmmmm(page)
});