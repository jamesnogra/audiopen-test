$(document).ready(function() {

    // Hide the popups
    $('.popup-container').hide()

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

    $('.popup-container').click(function() {
        $(this).hide()
    })
}) 

function closeAllPopups() {
    $('.popup-content-account').hide()
    $('.popup-content-settings').hide()
}