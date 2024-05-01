// at doucment ready, if id > 7, then add class 'trade-pad' and remove class 'page-nav-pad'


$(document).ready(function() {
    if (id >= 7) {
        $('.page-nav-pad').addClass('trade-pad');
        $('.page-nav-pad').removeClass('page-nav-pad');
    }
});