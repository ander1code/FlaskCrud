$(document).ready(() => {
    
    /* Messages */
    setTimeout(function() {
        $("#messages_info").fadeOut(5000);
    }, 5000);


    /* Modal */
    $("#modal").modal("show");
    $("#modal").on("hidden.bs.modal", ()=>{
        $.ajax({
            data:{},
            url:'clean_modal',
            method:'POST',
            success: function(response) {
            },
            error: function(xhr, status, error) {
            }
        })
    });

    /* Errors */
    setTimeout(function() {
        $("#errors_alert").fadeOut(5000);
    }, 5000);
    
});