(function($) {
    'use strict';

    // :: 10.0 Search Box Active Code
    $('#searchIcon').on('click', function() {
        $('.search-form').toggleClass('search-active');
    });
    $('.closeIcon').on('click', function() {
        $('.search-form').removeClass('search-active');
    });

})(jQuery);