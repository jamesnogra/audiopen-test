// Display timer variables
const duration = 5
let intervalId
let currentTimeDisplay = ''

// Recording controls
const startButton = document.getElementById('microphone')
const stopButton = document.getElementById('stop-recording')
const cancelRecordingButton = document.getElementById('icon-close-recorder')
let recordingStopped = false

// Recording audio variables
let audioRecorder
let audioChunks = []

navigator.mediaDevices.getUserMedia({ audio: true }).then(stream => {
    
        // Initialize the media recorder object
        audioRecorder = new MediaRecorder(stream)
        
        // dataavailable event is fired when the recording is stopped and data audio needs to be saved
        audioRecorder.addEventListener('dataavailable', e => {
            audioChunks.push(e.data)
            if (recordingStopped === false) {
                saveAndSendAudio()
            }
        })
        
        // start recording when the start button is clicked
        startButton.addEventListener('click', () => {
            recordingStopped = false
            // Stop any current running recording
            if (audioRecorder !== null && audioRecorder.state === "recording") {
                audioRecorder.stop()
            }
            // Show recording popup
            $('.popup-container').show()
            closeAllPopups()
            $('.popup-recorder').show()
            // Show timer for the recording popup
            $('#timer').html(minutesAndSecondsFormatter(duration))
            clearInterval(intervalId)
            startTimer(duration)
            // Start the recording
            audioChunks = []
            audioRecorder.start()
        })
        
        // stop recording when the stop button is clicked
        stopButton.addEventListener('click', () => {
            audioRecorder.stop()
        })

        // When x icon in the recorder is clicked, close the recorder popup
        cancelRecordingButton.addEventListener('click', () => {
            audioRecorder.stop()
            recordingStopped = true
            clearInterval(intervalId)
            $('.popup-container').hide()
        })

    }).catch(err => {
        // If the user denies permission to record audio, then display an error.
        console.log('Error: ' + err)
    }
)

function saveAndSendAudio() {
    startTranscribing()
    const blobObj = new Blob(audioChunks, { type: 'audio/webm' })
    const formData = new FormData()
    clearInterval(intervalId)
    formData.append('audio', blobObj, 'recorded_audio.wav')
    fetch('/upload-and-transcribe-audio', {
        method: 'POST',
        body: formData,
    }).then(response => {
        console.log("Audio sent successfully!", response)
    }).catch(error => {
        console.error("Error sending audio:", error)
    })
}

function startTranscribing() {
    $('.popup-recorder').hide()
    $('.popup-transcribing').show()
}

function startTimer(duration) {
    let timer = duration
    intervalId = setInterval(function () {
        currentTimeDisplay = minutesAndSecondsFormatter(timer)
        if (--timer < 0) { // Stop timer and recording
            clearInterval(intervalId)
            currentTimeDisplay = '00:00'
            stopButton.click()
        }
        $('#timer').html(currentTimeDisplay)
    }, 1000)
}

function stopTimer() {
    clearInterval(intervalId) // Stop timer
}

function minutesAndSecondsFormatter(timer) {
    let minutes, seconds
    minutes = parseInt(timer / 60, 10)
    seconds = parseInt(timer % 60, 10)
    minutes = minutes < 10 ? "0" + minutes : minutes
    seconds = seconds < 10 ? "0" + seconds : seconds
    return minutes + ":" + seconds
}