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

$("#staticBackdrop").on("show.bs.modal",function(event){
    target_id = $(event.relatedTarget).closest(".modal").attr("data-target");
    if(target_id){
        // 게시글 수정
        console.log("edit");
        $(this).find(".modal-title").text("게시글 수정");
        let form_url = '/feed/update/'+target_id
        $(this).find("form").attr("action",form_url);
        let form_content = $("#feed_"+target_id).find(".feed_content_text").text();
        $(this).find("form textarea").val(form_content);

    }else{
        console.log("create");
        $(this).find(".modal-title").text("게시글 작성");
        let form_url = '/feed/create/'
        $(this).find("form").attr("action",form_url);
        $(this).find("form textarea").val("");
    }
});