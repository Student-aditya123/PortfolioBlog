async function sendMessage() {

    const input = document.getElementById("chatbot-input");
    const message = input.value;

    if (!message) return;

    addUserMessage(message);

    input.value = "";

    const response = await fetch("/api/chatbot/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCookie("csrftoken")
        },
        body: JSON.stringify({
            message: message
        })
    });

    const data = await response.json();

    addBotMessage(data.response);
}