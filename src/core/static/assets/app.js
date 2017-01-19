$(document).ready(function() {
    // ------ STAFF SPOILER ------ //
    $('.staff-spoiler__button .button').click(function(){
        if ($(this).hasClass('showed')) {
            $('.staff-spoiler__content').slideUp(500);
            $(this).text('Показать всех сотрудников');
            $(this).removeClass('showed');
        } else {
            $('.staff-spoiler__content').slideDown(500);
            $(this).text('Свернуть');
            $(this).addClass('showed');
        }
        return false;
    });
});


// ------ TABS ------ //
$(document).ready(function(){
    $('.tab-menu__item:first-child a').addClass('tab-menu__text_active');
    $('.tab-item').first().css({'display':'block'});

    $('.tab-menu a').click(function(e) {
        e.preventDefault();
        $('.tab-menu__item .tab-menu__text_active').removeClass('tab-menu__text_active');
        $(this).addClass('tab-menu__text_active');

        var tab = $(this).attr('href');
        $('.tab-item').not(tab).css({'display':'none'});
        $(tab).fadeIn(200);
        return false;
    });
});

// ------ SPOILER ------ //
$(document).ready(function() {
    $('.spoiler .spoiler__text').click(function(e){
        e.preventDefault();
        if ($(this).hasClass('showed')) {
            $(this).next('.spoiler__content').slideUp(500);
            $(this).removeClass('showed');
        } else {
            $(this).next('.spoiler__content').slideDown(500);
            $(this).addClass('showed');
        }
        return false;
    });
});

$(document).ready(function () {
    $('#up').click(function(e) {
        e.preventDefault();
        $('html, body').animate({scrollTop: 0}, 1000);
        return false;
    })
});

$(document).ready(function(){
    $('.main-nav__item').mouseenter(function(){
        $(this).children('.main-nav__sub').slideDown('normal');
    });
    $('.main-nav__item').mouseleave(function(){
        $(this).children('.main-nav__sub').slideUp('normal');
    });
});