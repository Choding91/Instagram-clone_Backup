// card_feed 모달 
$('#feedMoreModel').on('show.bs.modal', function(event) {          
    target_id = $(event.relatedTarget).data('notifyid');
    target_auth = $(event.relatedTarget).data('auth');

    if(target_auth){
       
        $(this).find(".btn_edit").show();
        $(this).find(".btn_deletemodel").show();
        $(this).find(".btn_unfollow").hide();
    }else{
        $(this).find(".btn_edit").hide();
        $(this).find(".btn_deletemodel").hide();
        $(this).find(".btn_unfollow").show();
    }
    $(this).attr("data-target",target_id);
    $(this).find(".btn_goFeed").attr("onclick","location.href='/feed/"+target_id+"'");
});

$('#deleteModal').on('show.bs.modal', function(event) {     
    target_id = $(event.relatedTarget).closest(".modal").attr("data-target")
    $(this).find(".btn_delete").attr("onclick","location.href='/feed/delete/"+target_id+"'");
});