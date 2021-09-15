const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

$('#deleteVideoModal').on('shown.bs.modal', e => {
    var video_id = $(e.relatedTarget).data('id');

    $('#yes').on('click', e => {
        console.log(video_id);
        $.ajax({
            type: 'POST',
            url: "deleteVideo",
            headers: { 'X-CSRFToken': csrftoken },
            data: {
                video_id: video_id
            },
            success: function (response) {
                location.reload();
            },
            error: function (response) {
                // alert the error if any error occured
                // console.log(response);
            }
        })
    })
})