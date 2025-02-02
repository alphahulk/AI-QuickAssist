// popup.js - Handles fetching AI response and updating the UI
document.addEventListener("DOMContentLoaded", function () {
    chrome.storage.local.get("selectedText", function (data) {
        if (data.selectedText) {
            document.getElementById("selected-text").innerText = data.selectedText;
            fetchLLMResponse(data.selectedText);
        }
    });
});

function fetchLLMResponse(text) {
    const responseContainer = document.getElementById("response-container");
    responseContainer.innerText = "Loading AI response...";
    responseContainer.classList.add("loading");

    fetch("http://localhost:5000/ai-response", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: text })
    })
    .then(response => response.json())
    .then(data => {
        responseContainer.innerText = data.response;
        responseContainer.classList.remove("loading");
    })
    .catch(error => {
        responseContainer.innerText = "Error fetching AI response";
        responseContainer.classList.remove("loading");
        console.error("Error:", error);
    });
}
