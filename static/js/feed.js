// card_feed 모달 
$('#feedMoreModel').on('show.bs.modal', function(event) {          
    target_id = $(event.relatedTarget).data('notifyid');
    console.log(target_id)

    $(this).attr("data-target",target_id);

    $(this).find(".btn_delete").attr("onclick","location.href='/feed/delete/"+target_id+"'");
    $(this).find(".btn_goFeed").attr("onclick","location.href='/feed/"+target_id+"'");
});