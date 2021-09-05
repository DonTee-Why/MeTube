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

var isStarted, isStarted, isCompleted = false;
var timeStarted = -1
var timePlayed = 0;
player.on('playing', evemt => {
    timeStarted = new Date().getTime() / 1000;
    isStarted = true;

    paused();
    ended();
    updateViewed();
})

//Get the time played (in seconds) when the video is paused
function paused() {
    player.on('pause', event => {
        if (timeStarted > 0) {
            var timePlayedFor = new Date().getTime() / 1000 - timeStarted;
            timeStarted = -1;
            // add the new ammount of seconds played
            timePlayed += timePlayedFor;
        }
        console.log(`Video Paused, Time Played -> ${timePlayed}`)
    })
}

//Check if the video was watched completely without skipping
function ended() {
    player.on('ended', event => {
        if (!isCompleted && timePlayed >= player.duration) {
            console.log('COMPLETED!!');
            isCompleted = true;
        }
    })
}

//Check if video was watched for at least up to 30 secs in total then update view status
function updateViewed() {
    if (!isStarted && (timePlayed > 30)) {
        console.log('VIEWED!!');
        isStarted = true;
    }
}
