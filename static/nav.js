
function navHighlight() {
    let path = window.location.pathname;
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
        if (num < 1) {
            target = $('#n-basics');
        }
        else if (num < 6) {
            target = $('#n-patterns');
        }
        else {
            target = $('#n-trading');
        }
    }
    else if (page == 'quiz') {
        target = $('#n-quiz');
    }
    else if (page == 'introduction_chart') {
        target = $('#n-patterns');
    }
    else if (page == 'introduction_trade') {
        target = $('#n-trading');
    }
    target.removeClass('n-color');
    target.addClass('n-current');
}


$(document).ready(function() {
    navHighlight();
});
