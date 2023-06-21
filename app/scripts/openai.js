document.addEventListener('DOMContentLoaded', function() {
    var apiForm = document.getElementById('api-form');
    var chatList = document.getElementById('chat-list');

    apiForm.addEventListener('submit', function(e) {
        e.preventDefault();
        var userInput = document.getElementById('user-input').value;
        makeAPICall(userInput);
    });

    function makeAPICall(input) {
        var xhr = new XMLHttpRequest();
        xhr.open('POST', '/process');
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        xhr.onload = function() {
            if (xhr.status === 200) {
                updateChatBox(xhr.responseText);
            } else {
                console.error('API call failed:', xhr.status);
            }
        };
        xhr.send('user_input=' + encodeURIComponent(input));
    }

    function updateChatBox(response) {
        var chatItem = document.createElement('li');
        chatItem.textContent = response;
        chatList.appendChild(chatItem);
    }
});