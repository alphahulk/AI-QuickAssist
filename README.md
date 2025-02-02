# AI-QuickAssist
This Chrome extension allows you to easily select any text from any webpage and instantly assist to perform a variety of tasks 



# AI Popup Assistant - Chrome Extension

## Overview
AI Popup Assistant is a Chrome extension that helps users get AI-generated responses for selected text from websites, PDFs, or other text sources. This extension integrates with popular AI APIs like Claude, GPT, Gemini, or Grok to enhance user productivity.

## Features
- Select any text on a webpage and get AI-generated explanations.
- Supports multiple AI providers (GPT, Gemini, Claude, Grok).
- Simple UI with a popup for easy access.
- Copy AI-generated responses with one click.
- Fully customizable API key and endpoint.

---

## Installation Guide

### Step 1: Download the Extension Files
- Clone this repository:
  ```bash
  git clone https://github.com/your-username/ai-popup-extension.git
Step 2: Open the Chrome Extensions Page
Open Google Chrome.

chrome://extensions/

Step 3: Enable Developer Mode
Toggle the Developer mode switch (top-right corner).
Step 4: Load the Extension
Click Load unpacked.
Select the extracted extension folder.
Step 5: Verify Installation
The extension should now be visible in the Extensions list.
If there are errors, ensure manifest.json is correctly configured.


/ai-popup-extension
├── manifest.json       # Chrome extension configuration
├── popup.html          # UI for the popup window
├── popup.js            # JavaScript for handling popup logic
├── background.js       # Handles background events
├── content.js          # Injects script into webpages
├── styles.css          # Styles for the popup UI
├── README.md           # Documentation (this file)
└── icons/              # Extension icons




Contributing
Fork the repository.

Create a new branch:
git checkout -b feature-new-functionality

Commit changes and push:
git commit -m "Added new feature"
git push origin feature-new-functionality
Create a Pull Request on GitHub.
