$(document).ready(function () {
    $('#suggestion').keyup(function () {
        var query;
        query = $(this).val();
        $.get('/rango/suggest/', { suggestion: query }, function (data) {
            $('#cats').html(data);
        });
    });
    
    $('#likes').click(function () {
        var catid;
        catid = $(this).attr("data-catid");
        $.get('/rango/like', { category_id: catid }, function (data) {
            $('#like_count').html(data);
            $('#likes').hide();
        });
    });
    
    $('.rango_add').click(function () {
        var catid = $(this).attr("data-catid");
        var url = $(this).attr("data-url");
        var title = $(this).attr("data-title");
        var me = $(this)
        $.get('/rango/add/',
            { category_id: catid, url: url, title: tile }, function (data) {
                $('#pages').html(data);
                me.hide();
            });
    });
});