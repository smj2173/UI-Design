
function myFunction() {
    if (confirm("Are you sure you want to disregard your changes?")) {
        window.location.href = 'http://127.0.0.1:5000/view/'+id
    } 
    else {
        //keep changes there
    }
}

function edit_item(edited_item, id){
    $.ajax({
        type: "POST",
        url: '/edit_entry',
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        data: JSON.stringify(edited_item),
        success: function(result){
            let all_data = result["data"]
            let id = result["id"]
            data = all_data
            console.log(result)
            window.location.href = 'http://127.0.0.1:5000/view/'+id

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

    $("#save").click(function(){

        input_features_e = $("#fea_e").val();
        input_stores_e = $("#s_e").val();
        input_features_e = input_features_e.replace(/[\[\]']+/g,'') //brackets
        input_stores_e = input_stores_e.replace(/[\[\]']+/g,'') 
        input_features_e = input_features_e.replace(/["']/g, ''); //quotation
        input_stores_e = input_stores_e.replace(/["']/g, '');
        list_features_e = input_features_e.split(',')
        list_stores_e = input_stores_e.split(',')

        edited_item = {
                "id": id,
                "flavor" : $("#flav_e").val(),
                "description": $("#des_e").val(),
                "price": $("#price_e").val(),
                "ingredients": $("#ingred_e").val(),
                "features": list_features_e,
                "photo": $("#pic_e").val(),
                "rating": $("#rate_e").val(),
                "calories":$("#caloric_e").val(),
                "stores": list_stores_e,
        }

        edit_item(edited_item, id)
    });

});
