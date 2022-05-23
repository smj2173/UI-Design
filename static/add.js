
function is_blank(input, id){
    val = (input).val()
    if (val.trim().length === 0){
        error_box_name = id+"-e"
        $("#"+(error_box_name).toString()).append("Input is blank")
        return true;
    }
    else{
        return false;
    }
}

function add_item(new_item){
    $.ajax({
        type: "POST",
        url: "add_entry",
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        data: JSON.stringify(new_item),
        success: function(result){
            let all_data = result["data"]
            let id = result["temp_id"]
            data = all_data
            href = "/view/"+id
            $("#put_result").empty()
            $("#put_result").append("<div>New item successfully created</div>")
            $("#put_result").append("<div><a class = 'mytext' href ="+href+">See it here.</a></div>")
            $('#flav').val('')
            $('#des').val('')
            $('#ingred').val('')
            $('#s').val('')
            $('#rate').val('')
            $('#pic').val('')
            $('#fea').val('')
            $('#price').val('')
            $('#caloric').val('')
            $("#flav").focus();
            $("#1-e").empty();
            $("#2-e").empty();
            $("#3-e").empty();
            $("#4-e").empty();
            $("#5-e").empty();
            $("#6-e").empty();
            $("#8-e").empty();
            $("#9-e").empty();
        },
        error: function(request, status, error){
            console.log("Error")
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}

$(document).ready(function(){
    $("#sub").click(function(){
        has_errors = false;
        if (is_blank($("#flav"), 1) === true){
            has_errors = true;
        }
        if (is_blank($("#des"), 2)){
            has_errors = true;
        }
        if (is_blank($("#price"), 3)){
            has_errors = true;
        }
        if (is_blank($("#ingred"), 4)){
            has_errors = true;
        }
        if (is_blank($("#pic"), 6)){
            has_errors = true;
        }
        if (is_blank($("#caloric"), 8)){
            has_errors = true;
        }

        if (has_errors === true){
            //do nothing
        }
        else{ //no errors, submit
            // fix lists



            new_item = {

                "flavor" : $("#flav").val(),
                "description": $("#des").val(),
                "price": $("#price").val(),
                "ingredients": $("#ingred").val(),
                "features": $("#fea").val(),
                "photo": $("#pic").val(),
                "rating": $("#rate").val(),
                "calories":$("#caloric").val(),
                "stores": $("#s").val(),
            }
            add_item(new_item)
        }
       
    });




});