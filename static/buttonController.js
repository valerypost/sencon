/**
 * Created by val on 2017-02-25.
 */
$(document).ready(function () {
    console.log("loaddd");

    $('#feed').on('click', function (e) {
            e.preventDefault();
            e.stopPropagation();
            console.log("feed");

        }
    )
    function callBackChange(value) {
        console.log("powerfff:" + value);
        var arr = { power:value, offTimer: 25 };
        $.ajax({
            url: 'data',
            type: 'POST',
            data: JSON.stringify(arr),
            contentType: 'application/json; charset=utf-8',
            dataType: 'json',
            async: false,
            success: function (msg) {
                console.log(msg);
            }
        });

        console.log(value);
    }
    var callbacks = $.Callbacks();
        callbacks.add(callBackChange);

    $("#power").on("change", function (e) {
        e.preventDefault();
        e.stopPropagation();


        callbacks.fire($("#power").prop("checked"));



    });

});