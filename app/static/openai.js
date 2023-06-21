function submitForm(event) {
    event.preventDefault(); // Prevent default form submission
    var userInput = document.getElementById('user-input').value;
    makeAPICall(userInput);
    document.getElementById('user-input').value = ''; // Clear the input field
    return false;
}

function makeAPICall(input) {
    fetch('/process', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: 'user_input=' + encodeURIComponent(input)
    })
    .then(function(response) {
        if (response.ok) {
            return response.text();
        } else {
            throw new Error('API call failed: ' + response.status);
        }
    })
    .then(function(data) {
        updateChatBox(data);
    })
    .catch(function(error) {
        console.error('Fetch error:', error);
    });
}

function updateChatBox(response) {
    var chatMessages = document.getElementById('chat-messages');
    var chatItem = document.createElement('li');
    chatItem.textContent = response;
    chatMessages.appendChild(chatItem);
}

document.getElementById('api-form').addEventListener('submit', submitForm);