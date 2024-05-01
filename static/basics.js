function addClickEventToButtons(defintions) {
    // understand which button was clicked that has the class 'toggleButton'
    let buttons = $('.toggleButton');
    buttons.each(function() {
        $(this).click(function() {
            let id = $(this).attr('id');
            // make background color green
            $(this).css('background-color', 'green');
            // make text color white
            $(this).css('color', 'white');
            // make all other buttons background color body color
            buttons.each(function() {
                if ($(this).attr('id') !== id) {
                    $(this).css('background-color', 'aliceblue');
                    $(this).css('color' , '#6c757d');
                }
            });
            // string is substring of id from 1 to end
            let def = defintions[id.substring(1)];
            $('.main-cont').empty();
            let inn_html = '<div class="def-box">'+ def + '</div>';
            $('.main-cont').append(inn_html);
            // show the definition box
            $('.main-cont').show();
        });
    });

}

$(document).ready(function() {
    let defintions = {
        'stock' : 'A piece of a company that people can buy, own, or sell.',
        'buy' : 'The act of purchasing shares in a company.',
        'sell' : 'The act of selling owned shares in a company.',
        'long-term' : 'Holding stocks or assets over a long period of time.',
        'short-term' : 'A measure of time in trading that typically means holding an asset for a short period.',
        'share' : 'A single unit of ownership in a company or financial asset.',
        'trade' : 'The act of buying or selling in the stock market.'
    };
    $('.main-cont').append('<div class="def-box" style="color: red;">Click on a term to see its definition.</div>');
    $('#xstock, #xbuy, #xsell, #xlong-term, #xshort-term, #xshare, #xtrade').addClass('xpad');
    var maxWidth = 0;

    $('.toggleButton').each(function() {
        var width = $(this).outerWidth();
        if (width > maxWidth) {
            maxWidth = width;
        }
    });
    addClickEventToButtons(defintions);

    $('.toggleButton').css('width', maxWidth);
});