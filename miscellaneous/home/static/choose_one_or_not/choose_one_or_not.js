$(function() {
    $('#radio').hide();
    $('#radioBoxB1').prop('disabled', true);
    $('#radioBoxB2').prop('disabled', true);

    $('#flexCheckDefault').click(function(event) {
        let is_checked = $(this).prop('checked');
        if (is_checked) {
            $('#radio').slideDown();
        } else {
            $('#radio').slideUp();
        }
    })

    $('#checkB').click(function(event) {
        let is_checked = $(this).prop('checked');
        if (is_checked) {
            $('#radioBoxB1').prop('disabled', false)
            $('#radioBoxB2').prop('disabled', false)
        } else {
            $('#radioBoxB1').prop('disabled', true)
            $('#radioBoxB2').prop('disabled', true)
        }
    })
})