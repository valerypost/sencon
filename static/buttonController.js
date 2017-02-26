/**
 * Created by val on 2017-02-25.
 */
$(document).ready(function () {
    console.log("loaddd");

    $('#feed').on('click', function (e) {
            e.preventDefault();
            e.stopPropagation();
            console.log("feed");
            callbacks.fire({command: "feeder",offTimer:1});

        }
    )
    function callBackChange(value) {
        var power = $("#power").prop("checked");
        console.log("powerfff:" + value);
        var arr = value;
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

        console.log();
    }
    var callbacks = $.Callbacks();
        callbacks.add(callBackChange);

    $("#power").on("change", function (e) {
        e.preventDefault();
        e.stopPropagation();


        var power = $("#power").prop("checked");
        if(power){

        }
        callbacks.fire({command: "power",offTimer:$("#offTimer").val()});



    });

});