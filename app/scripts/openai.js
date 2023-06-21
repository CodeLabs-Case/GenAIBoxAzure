$(document).ready(function() {
    $('#api-form').submit(function(e) {
        e.preventDefault();
        var userInput = $('#user-input').val();
        makeAPICall(userInput);
    });

    function makeAPICall(input) {
        // Make the API call using AJAX
        $.ajax({
            url: '/process',
            type: 'POST',
            data: { user_input: input },
            success: function(response) {
                updateChatBox(response);
            },
            error: function(error) {
                console.error('API call failed:', error);
            }
        });
    }

    function updateChatBox(response) {
        // Update the chat box content with the response
        $('.chat-box ul').html(response);
    }
});