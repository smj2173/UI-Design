


function display_three(data){
    $("#three").empty()
    i = 0 
    $.each(data, function(index, value){ //each dictionary
        i = i + 1
        href = '/view/'+i
        flav = value["flavor"]
        flav = flav.replaceAll('"', ''); //quotation
        to_append = "<div class = 'col-md-4'> <a href="+href+"><img class='img-fluid' src ="+value["photo"]+" alt='an image of the flavor "+flav+"'></a><a class = 'mytext' href ="+href+">"+flav+"</a><br></div>"
        $("#three").append(to_append)
        if (i > 2){
            return false;
        }
    });
}


$(document).ready(function(){
    display_three(data)

});
