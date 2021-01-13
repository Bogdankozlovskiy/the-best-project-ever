$('document').ready(function () {
    $('.like-comment').on('click', function () {
        let id=$(this).attr('id');
        $.ajax({
            url:"/shop/add_like2comment_ajax",
            data: {"comment_id": id.split('-')[1]},
            method: "GET",
            success: function (data) {
                $(`#${id}`).html(`Likes: ${data['likes']}`);
            }
        })
    });

    $('.delete-comment').on('click', function () {
        let id=$(this).attr('id');
        $.ajax({
            url: "/shop/delete_comment_ajax",
            data: {"comment_id": id.split("-")[2]},
            method: "GET",
            success: function (data) {
                $(`#${id}`).remove()
            }
        })
    })
});

