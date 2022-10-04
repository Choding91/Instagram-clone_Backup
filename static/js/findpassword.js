$('#button_findpassword').on('click', () => {
    let email = $('#floatingEmail').val();

    $.ajax({
        url: "/findpassword",
        data: {
            email: email,
        },
        method: "POST",
        dataType: "json",
        success: function (data) {
            alert(data.message);
            location.replace('signin');
        },
        error: function (request) {
            let data = JSON.parse(request.responseText);
            console.log(data.message);
            alert(data.message);
        }
    });
});