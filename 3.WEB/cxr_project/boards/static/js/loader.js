$(window).load(function(){
    $('#loading').delay('300').fadeOut()
})

function loading(){
    $("#loading").show();
    $("#loader_text").show();

    $(".container").hide(); 
}