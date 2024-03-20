$(document).ready(function() {
    $('.header-menu, .burger-menu__close').click(function(event) {
        $('.burger-menu__container').toggleClass('active');
        $('body').toggleClass('lock')
        $(".blackout").toggleClass('active');
        updateCursor();
    });

    $('.burger-menu__theme-light').click(function(event) {
        if($('body').hasClass('dark')){
            $('body').removeClass('dark');
            $('body').addClass('light');
            updateCursor();
            }else{
                $('body').addClass('light');
            }
    });


    $('.burger-menu__theme-dark').click(function(event) {
        if($('body').hasClass('light')){
            $('body').removeClass('light');
            $('body').addClass('dark');
            updateCursor();
            }else{
                $('body').addClass('dark');
            }
    });
    
    function updateCursor(){
        if($('body').hasClass('dark')){
            $('.burger-menu__theme-light').css('cursor', 'pointer');
            $('.burger-menu__theme-dark').css('cursor', 'default');
        }
        
        if($('body').hasClass('light')){
            $('.burger-menu__theme-dark').css('cursor', 'pointer');
            $('.burger-menu__theme-light').css('cursor', 'default');
        }
    }


});
$(document).mouseup(function (e){ // событие клика по веб-документу
    var div = $(".burger-menu__container"); // тут указываем ID элемента
    if($('body').hasClass('lock')){
        if (!div.is(e.target) // если клик был не по нашему блоку
            && div.has(e.target).length === 0) { // и не по его дочерним элементам
            div.css('translateX',"50%");
            $('body').removeClass('lock');
            $('.burger-menu__container').removeClass('active');
            $(".blackout").removeClass('active');
        }
    }});