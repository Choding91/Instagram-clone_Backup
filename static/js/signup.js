$('#button_signup').on('click', () => {
    let email = $('#floatingEmail').val();
    let name = $('#floatingName').val();
    let user_id = $('#floatingUserId').val();
    let password = $('#floatingPassword').val();

    $.ajax({
        url: "/signup",
        data: {
            email: email,
            password: password,
            user_id: user_id,
            name: name
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