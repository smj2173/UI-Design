
const salesperson = "Sophie Johnson"

$(function(){
    clients = [
        "Shake Shack",
        "Toast",
        "Computer Science Department",
        "Teacher's College",
        "Starbucks",
        "Subsconsious",
        "Flat Top",
        "Joe's Coffee",
        "Max Caffe",
        "Nussbaum & Wu",
        "Taco Bell",
    ]; 
    
    $("#client").autocomplete({
        source: clients
    });
})




var sales = [
        {
            "salesperson": "James D. Halpert",
            "client": "Shake Shack",
            "reams": 100
        },
        {
            "salesperson": "Stanley Hudson",
            "client": "Toast",
            "reams": 400
        },
        {
            "salesperson": "Michael G. Scott",
            "client": "Computer Science Department",
            "reams": 1000
        },
]


    function makeEntries(list){
        $("#posts").empty()
        $.each(list, function(index, value){ //each dictionary
            let button = "<button class = 'btn btn-primary delete' style = 'background-color:rgb(255, 208, 0); border-color:rgb(255, 208, 0)'>X</button>"
            let entry = "<div class = 'row record'> <div class = 'col-md-2'>"+ value["salesperson"] + 
            "</div> <div class = 'col-md-4'>" + value["client"] + "</div> <div class = 'col-md-2'>" + 
            value["reams"] + "</div><div>" + button + "</div></div>"
            $("#posts").append(entry)
            $("#posts").append("<br>")
        }); 
    }

    function newEntry(client, reams){
        const salesperson = "Sophie Johnson"
        temp = sales
        sales = []
        sales.push({
            "salesperson": salesperson,
            "client": client,
            "reams": reams
        });
        sales = sales.concat(temp)
        makeEntries(sales)
    }

    $(document).ready(function(){
        makeEntries(sales)


        
        $("#post").click(function(){
            var regExp = /[a-zA-Z]/g;
            if ($("#reams").val().length === 0 || $("#client").val().length === 0 || regExp.test($("#reams").val())){
                if ($("#client").val().length === 0){
                    $("#error_client").html("enter client name.");
                }
                if ($("#reams").val().length === 0){
                    $("#error_reams").html("enter ream value.");
                }
                if (regExp.test($("#reams").val())){
                    $("#error_reams").html("data entered is not a number");
                }
            }
            else{
                $("#error_client").html("");
                $("#error_reams").html("");
                newEntry($("#client").val(), $("#reams").val())
                $("#client").focus();
                if (clients.includes($("#client").val())){
                    //do nothing
                }
                else{
                    clients.push($("#client").val());
                    $("#client").autocomplete({
                        source: clients
                    });
                }
                $("#client").val('');
                $("#reams").val('');
            }
        });   
        
        $("#reams").keypress(function(event){
            if (event.keyCode === 13){
                if ($("#post").attr('disabled')){
                    //do nothing
                }   
                else{
                    $("#post").click();
                } 
            }
        })

        $(document).on("click", '.btn.btn-primary.delete', function(){
            let x = this.id
            if (sales !== -1){
                sales.splice(x, 1)
            }
            $(".record").remove()
            makeEntries(sales)
        });



    });






    