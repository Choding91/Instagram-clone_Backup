$('#button_signin').on('click', () => {
    let email = $('#floatingEmail').val();
    let password = $('#floatingPassword').val();

    $.ajax({
        url: "/signin",
        data: {
            email: email,
            password: password
        },
        method: "POST",
        dataType: "json",
        success: function (data) {
            alert(data.message);
            location.replace('/');
        },
        error: function (request) {
            let data = JSON.parse(request.responseText);
            console.log(data.message);
            alert(data.message);
        }
    });
});