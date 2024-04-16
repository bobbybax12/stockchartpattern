
function navHighlight() {
    let path = window.location.pathname;
    console.log(path);
    let x = path.split("/");
    let page = x[1];
    let num = -1;
    if (x.length > 2) {
        num = x[2];
    }
    let target = '';
    if (page == '') {
        target = $('#n-home');
    }
    else if (page == 'learn') {
        if (num < 2) {
            target = $('#n-basics');
        }
        else if (num < 9) {
            target = $('#n-patterns');
        }
        else {
            target = $('#n-trading');
        }
    }
    else {
        target = $('#n-quiz');
    }
    target.removeClass('n-color');
    target.addClass('n-current');
}


$(document).ready(function() {
    navHighlight();
});
