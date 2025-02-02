chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.action === "showPopup") {
        chrome.storage.local.set({ selectedText: message.text });
        chrome.action.openPopup();
    }
});