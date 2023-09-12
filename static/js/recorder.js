// Display timer variables
const duration = 10
let intervalId
let currentTimeDisplay = ''
// Recording audio variables
const audioChunks = []
let mediaRecorder

function startRecording() {
    askBrowserToUseMicrophone()
    $('#timer').html(minutesAndSecondsFormatter(duration))
    stopTimer()
    startTimer(duration)
}

// This function is only called when the user cancels recording and submission
function stopRecording() {
    if (mediaRecorder !== undefined) {
        mediaRecorder.stop()
    }
}

// When the actual stop icon is clicked
function stopAndSaveRecording() {
    if (mediaRecorder !== undefined) {
        mediaRecorder.stop()
        audioChunks.length = 0
        stopTimer()
        saveAndSendAudio()
    }
}

function saveAndSendAudio() {
    const audioBlob = new Blob(audioChunks, { type: 'audio/wav' })
    const formData = new FormData()
    formData.append('audio', audioBlob, 'recorded_audio.wav')
    fetch('/upload-and-transcribe-audio', {
        method: 'POST',
        body: formData,
    }).then(response => {
        console.log("Audio sent successfully!", response)
    }).catch(error => {
        console.error("Error sending audio:", error)
    })
}

// Ask permission to use microphone
function askBrowserToUseMicrophone() {
    navigator.mediaDevices.getUserMedia({ audio: true }).then(stream => {
        mediaRecorder = new MediaRecorder(stream)
        mediaRecorder.ondataavailable = event => {
            if (event.data.size > 0) {
                audioChunks.push(event.data)
            }
        }
        // Clear previous chunks every start of recording
        audioChunks.length = 0
        mediaRecorder.start()
        // Handle post-recording actions, if needed
        mediaRecorder.onstop = () => {}
        // On error
        mediaRecorder.onerror = (event) => {
            console.error("MediaRecorder error:", event.error)
        }
    }).catch(error => {
        console.error("Error accessing microphone:", error)
    })
}

function startTimer(duration) {
    let timer = duration
    intervalId = setInterval(function () {
        currentTimeDisplay = minutesAndSecondsFormatter(timer)
        if (--timer < 0) { // Stop timer and recording
            clearInterval(intervalId)
            currentTimeDisplay = '00:00'
            stopAndSaveRecording()
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