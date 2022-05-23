function display_rating(rating){
    $("#rating").empty()
    filled_stars = parseInt(rating)
    not_filled = 5 - filled_stars
    while (filled_stars > 0){
        $("#rating").append("<span class='fa fa-star checked'></span>")
        filled_stars = filled_stars - 1;
    }
    while (not_filled > 0){
        $("#rating").append("<span class='fa fa-star'></span>")
        not_filled = not_filled - 1;
    }
}

function print_stores(stores){
    if (stores.length === 0){
        //do nothing
    }
    else{
        $.each(stores, function(index, value){ //each dictionary
            v = value.toLowerCase()
            href = "/search_results/"+v
            to_append = "<div><a class='store' href="+href+">"+value+"</div>"
            $("#stores").append(to_append)
        });
    }
}

function features(features){
    console.log(features)
    if (features.length === 1 && features[0] === ""){
        //do nothing
    }
    else{
        $.each(features, function(index, value){
            href = "/search_results/"+value
            to_append = "<div class = 'col-md-3 f' ><a class='fe' href ="+href+">"+value+"</div>"
            $("#feat").append(to_append)
        });
    }   
}


$(document).ready(function(){
    display_rating(data[page]["rating"])
    print_stores(data[page]["stores"])
    features(data[page]["features"])
    if (data[page]["stores"].length === 0){
        $("#stores").append("<div>Not Available Nearby")
    }

});
