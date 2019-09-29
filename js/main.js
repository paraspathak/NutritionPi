$(document).ready(function () {
    $.ajax({
        url: '/takephoto',
        type: 'POST',
        data: JSON.stringify('start'),
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        success: function (msg) {
            console.log(msg);
        }
    });
});


