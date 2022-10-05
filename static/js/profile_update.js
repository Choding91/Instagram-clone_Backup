$('#submit').on('click', () => {
    let name = $('#floatingName').val();
    let username = $('#floatingUsername').val();
    let website = $('#floatingWebsite').val();
    let bio = $('#floatingBio').val();
    let email = $('#floatingEmail').val();
    let phone = $('#floatingPhone').val();

    $.ajax({
        url: "/profile_update/",
        data: {
            name: name,
            username: username,
            website: website,
            bio: bio,
            email: email,
            phone: phone
        },
        method: "POST",
        dataType: "json",
        success: function (data) {
            alert(data.message);
            location.replace('/profile');
        },
        error: function (request) {
            let data = JSON.parse(request.responseText);
            console.log(data.message);
            alert(data.message);
        }
    });
});