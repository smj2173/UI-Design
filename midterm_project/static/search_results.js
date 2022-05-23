

$(document).ready(function(){
if (Object.keys(results).length === 0){
    //meaning no results found
    $("#results").append("No results found")
}
   
else{
    num = Object.keys(results).length
    $("#h").append("<div>"+num+" Search Results for '"+search_string+"'</div>")
    for (const [key, value] of Object.entries(results)){
        href = '/view/'+key
        pic = data[key]["photo"]
        to_append = "<div><a href="+href+"><img class='search_img' src="+pic+" alt='an image of the flavor"+value+"'></a><a class = 'mytext' href ="+href+">"+value+"</a></div><br>"
        $("#results").append(to_append)
    }
}
});
    