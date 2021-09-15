//Note: Time is in seconds
var controls =
    [
        'play-large', // The large play button in the center
        //'restart', // Restart playback
        //'rewind', // Rewind by the seek time (default 10 seconds)
        'play', // Play/pause playback
        'fast-forward', // Fast forward by the seek time (default 10 seconds)
        'progress', // The progress bar and scrubber for playback and buffering
        'current-time', // The current time of playback
        'duration', // The full duration of the media
        'mute', // Toggle mute
        'volume', // Volume control
        'captions', // Toggle captions
        'settings', // Settings menu
        'pip', // Picture-in-picture (currently Safari only)
        //'airplay', // Airplay (currently Safari only)
        //'download', // Show a download button with a link to either the current source or a custom URL you specify in your options
        'fullscreen' // Toggle fullscreen
    ];

const player = new Plyr('#player', {
    controls,
    hideControls: true,
    keyboard: {
        focused: true,
        global: false
    },
    tooltips: {
        controls: true,
        seek: true
    }
});

var isStarted, isCompleted, isViewed = false;
var timeStarted = -1;
var timePlayed = 0;
player.on('playing', event => {
    timeStarted = new Date().getTime() / 1000;
    isStarted = true;

    //Get the time played (in seconds) when the video is paused
    player.on('pause', event => {
        trackWatchTime(event);
    })

    //Check if the video was watched completely without skipping
    player.on('ended', event => {
        console.log('COMPLETED!!');
        if (!isCompleted && timePlayed >= player.duration) {
            console.log('COMPLETED!!');
            isCompleted = true;
        }
    })

    //Check if video was watched for at least up to 30 secs in total then update view status
    player.on('timeupdate', event => {
        trackWatchTime(event);
    })
})

function trackWatchTime(event) {
    if (timeStarted > 0) {
        var timePlayedFor = Math.round((new Date().getTime() / 1000 - timeStarted) * 100) / 100;
        timeStarted = -1;

        // add the new ammount of seconds played
        timePlayed += timePlayedFor;
        timeStarted = new Date().getTime() / 1000;
        if (event.type == 'timeupdate' && !isViewed && (timePlayed > 30)) {
            // console.log('VIEWED!!');
            isViewed = true;

            const video_id = document.querySelector('[name=video_id]').value;
            const user_id = document.querySelector('[name=user_id]').value;
            const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
            //update video views
            $.ajax({
                type: 'POST',
                url: "updateView",
                headers: { 'X-CSRFToken': csrftoken },
                data: {
                    video_id: video_id,
                    user_id: user_id
                },
                success: function (response) {
                    // console.log(response)
                },
                error: function (response) {
                    // alert the error if any error occured
                    // console.log(response);
                }
            })
        }
    }
}


