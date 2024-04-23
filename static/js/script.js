$(document).ready(function () {
    $('.header-menu').click(function (event) {
        $('.burger-menu__container').addClass('active');
        $('body').css('overflow', "hidden");
        $(".blackout").addClass('active');
        updateCursor();
    });

    $('.changeThemeButton').click(function() {
        var theme = $(this).data('theme');
        var csrftoken = $('#changeThemeForm [name=csrfmiddlewaretoken]').val();
            var url = $(this).data('url')
        $.ajax({
            type: 'POST',
            url: url,
            data: {
                'theme': theme,
                'csrfmiddlewaretoken': csrftoken,
            },
            dataType: 'json',
            success: function(response) {
                if ($('body').hasClass('dark')) {
                    $('body').removeClass('dark');
                    $('body').addClass('light');
                    updateCursor();
                    $('.burger-menu__theme-light').prop('disabled', true);
                    $('.burger-menu__theme-dark').prop('disabled', false);
                } else {
                    if ($('body').hasClass('light')) {
                        $('body').removeClass('light');
                        $('body').addClass('dark');
                        updateCursor();
                        $('.burger-menu__theme-dark').prop('disabled', true);
                        $('.burger-menu__theme-light').prop('disabled', false);
                }}
            },
        });
    });


    function updateCursor() {
        if ($('body').hasClass('dark')) {
            $('.burger-menu__theme-light').css('cursor', 'pointer');
            $('.burger-menu__theme-dark').css('cursor', 'default');
        }
        if ($('body').hasClass('light')) {
            $('.burger-menu__theme-dark').css('cursor', 'pointer');
            $('.burger-menu__theme-light').css('cursor', 'default');
        }
    };

    $('.burger-menu__close').click(function (event) {
        $('.burger-menu__container').removeClass('active');
        $('body').css('overflow-y', "visible");
        $(".blackout").removeClass('active');
    }
    );

    $('.header-button').click(function (event) {
        $('body').css('overflow-y', "hidden");
        $('.catalog-menu-container').addClass('active');
        $(".blackout").addClass('active');
    });



}
);

$(document).mouseup(function (e) {
    var div = $(".burger-menu__container");

    if ($(div).hasClass('active')) {
        if (!div.is(e.target) // если клик был не по нашему блоку
            && div.has(e.target).length === 0) { // и не по его дочерним элементам
            $('body').css('overflow-y', "visible");
            $(div).removeClass('active');
            $(".blackout").removeClass('active');
        }
    } else {
        var div2 = $(".catalog-menu-container");
        if ($(div2).hasClass('active')) {
            if (!div2.is(e.target)
                && div2.has(e.target).length === 0) {
                $(div2).removeClass('active');
                $('body').css('overflow-y', "visible");
                $(".blackout").removeClass('active');
            }
        } 
    }
}
);
$(document).on('click', function (e) {
    var target = $(e.target);
    
    // Перевіряємо, чи був клік здійснений на кнопці .sort-limit-btn
    if (target.hasClass('sort-limit-btn')) {
        target.next('.sort-limit__row').toggleClass('active');
        target.next('.sort-limit__row')[0].offsetHeight;
    } else {
        // Перевіряємо, чи клік був здійснений поза .sort-limit__row
        if (!target.closest('.sort-limit__row').length) {
            $('.sort-limit__row').removeClass('active');
        }
    }
});
