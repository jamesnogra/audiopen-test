// Display timer variables
const duration = 180
let intervalId
let currentTimeDisplay = ''

// Recording controls
const startButton = document.getElementById('microphone')
const stopButton = document.getElementById('stop-recording')
const cancelRecordingButton = document.getElementById('icon-close-recorder')
const popupWhiteBg = document.getElementById('popup-white-opaque')
let recordingStopped = false

// Recording audio variables
let audioRecorder
let audioChunks = []
let stream

// start recording when the start button is clicked
startButton.addEventListener('click', async () => {
    stream = await navigator.mediaDevices.getUserMedia({ audio: true })
    audioRecorder = new MediaRecorder(stream)
    startRecordingAudio()
})

// stop recording when the stop button is clicked
stopButton.addEventListener('click', () => {
    const tracks = stream.getTracks()
    tracks.forEach(track => track.stop())
})

// When x icon in the recorder is clicked, close the recorder popup
cancelRecordingButton.addEventListener('click', () => {
    cancelRecording()
})
// Same with clicking the white popup opaque background, cancel recording
popupWhiteBg.addEventListener('click', () => {
    cancelRecording()
})

// Start recording function
function startRecordingAudio() {
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
    stopTimer()
    startTimer(duration)
    // Start the recording
    audioChunks = []
    audioRecorder.start()
    // dataavailable event is fired when the recording is stopped and data audio needs to be saved
    audioRecorder.addEventListener('dataavailable', e => {
        audioChunks.push(e.data)
        if (recordingStopped === false) {
            saveAndSendAudio()
        }
    })
}

// Cancels a recording, do not save and transcribe the audio
function cancelRecording() {
    audioRecorder.stop()
    recordingStopped = true
    stopTimer()
    $('.popup-container').hide()
}

// Saves the recording audtio and sends it to the flask service for transciptions
function saveAndSendAudio() {
    showStartTranscribingUi()
    const blobObj = new Blob(audioChunks, { type: 'audio/webm' })
    const formData = new FormData()
    stopTimer()
    formData.append('audio', blobObj, 'recorded_audio.webm')
    fetch('/upload-and-transcribe-audio', {
        method: 'POST',
        body: formData,
    }).then(response => {
        // Success in sending audio
        // Check if the response status is OK (200)
        if (response.status === 200) {
            return response.json() // Parse the JSON response
        } else {
            throw new Error('Error: ' + response.statusText)
        }
    }).then(data => {
        // Success in sending audio, access the data
        showOutputPopup(data)
        
    }).catch(error => {
        console.error("Error sending audio:", error)
    })
}

// Shows the popup UI for the output
function showOutputPopup(data) {
    closeAllPopups()
    $('.popup-container').hide()
    $('.popup-output-container').show() // Show the output popup
    $('.popup-original-transcript-content').hide() // Hide the original text by default
    // Put the output on the html elements
    $('.popup-output-title').html(data.gpt_title)
    $('.popup-output-date').html(data.date)
    $('.popup-output-summary').html(data.gpt_summary_text)
    $('.popup-original-transcript-content').html(data.full_transcribed_text)
}

// Shows the popup UI for the transcribing of audio to text
function showStartTranscribingUi() {
    $('.middle-container-recorder').hide()
    $('.middle-container-transcribing').show()
}

// Starts the timer of the recorder
function startTimer(duration) {
    let timer = duration
    intervalId = setInterval(function () {
        currentTimeDisplay = minutesAndSecondsFormatter(timer)
        if (--timer < 0) { // Stop timer and recording
            stopTimer()
            currentTimeDisplay = '00:00'
            stopButton.click()
        }
        $('#timer').html(currentTimeDisplay)
    }, 1000)
}

// Stops the timer of the recorder and clears the interval
function stopTimer() {
    clearInterval(intervalId) // Stop timer
}

// Formats the display timer of the recorder to minutes and seconds
function minutesAndSecondsFormatter(timer) {
    let minutes, seconds
    minutes = parseInt(timer / 60, 10)
    seconds = parseInt(timer % 60, 10)
    minutes = minutes < 10 ? "0" + minutes : minutes
    seconds = seconds < 10 ? "0" + seconds : seconds
    return minutes + ":" + seconds
}