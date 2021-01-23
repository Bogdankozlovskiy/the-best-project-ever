function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');




$('document').ready(function () {
    $('.like-comment').on('click', function () {
        let id=$(this).attr('id');
        let current_id = id.split('-')[1];
        $.ajax({
            url:`/shop/add_like2comment_ajax/${current_id}`,
            headers: { 'X-CSRFToken': csrftoken},
            method: "POST",
            success: function (data) {
                $(`#${id}`).html(`Likes: ${data['likes']}`);
            }
        })
    });

    $('.delete-comment').on('click', function () {
        let id=$(this).attr('id');
        let comment_id = id.split("-")[2];
        $.ajax({
            url: `/shop/delete_comment_ajax/${comment_id}`,
            method: "DELETE",
            headers: { 'X-CSRFToken': csrftoken},
            success: function (data) {
                $(`#${id}`).remove()
            }
        })
    })
});

