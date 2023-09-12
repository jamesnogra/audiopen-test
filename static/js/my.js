$(document).ready(function() {

    // Hide the popups
    $('.popup-container').hide()

    // Click on microphone icon
    $('#microphone').click(function() {
        $('.popup-container').show()
        closeAllPopups()
        $('.popup-recorder').show()
    })

    // When x icon in the recorder is clicked, close the recorder popup
    $('#icon-close-recorder').click(function() {
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
}) 

function closeAllPopups() {
    $('.popup-content-account').hide()
    $('.popup-content-settings').hide()
    $('.popup-recorder').hide()
}