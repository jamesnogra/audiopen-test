$(document).ready(function() {

    // Hide the popups
    $('.popup-container').hide()
    // Hide the output popup
    $('.popup-output-container').hide()

    // Cancel transcribing audio to text
    $('#cancel-transcribing').click(function() {
        closeAllPopups()
        $('.popup-container').hide()
    })

    // Click account icon
    $('#icon-account').click(function() {
        $('.popup-container').show()
        closeAllPopups()
        $('.popup-content-account').show()
    })

    // Click on settings icon
    $('#icon-settings').click(function() {
        $('.popup-container').show()
        closeAllPopups()
        $('.popup-content-settings').show()
    })

    // When opaque background is clicked, close all popups
    $('.popup-container').click(function(e) {
        if (e.target.classList.contains('popup-white-opaque')) {
            $(this).hide()
        }
    })

    // Output transcript toggle original text from audio
    $('.popup-original-transcript-toggle').click(function() {
        const transcriptContent = $('.popup-original-transcript-content')
        if (transcriptContent.is(':visible')) {
            transcriptContent.hide('fast', 'swing')
            $('.popup-original-transcript-toggle').html('show original transcript')
        } else {
            transcriptContent.show('show', 'swing')
            $('.popup-original-transcript-toggle').html('hide original transcript')
        }
    })
}) 

function closeAllPopups() {
    $('.popup-content-account').hide()
    $('.popup-content-settings').hide()
    $('.popup-recorder').hide()
    $('.middle-container-transcribing').hide()
    $('.popup-output-container').hide()
}