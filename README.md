# Repository for final project
AI Emotion Detection Web App
AI-powered emotion detection web application with a cyberpunk-inspired modern UI. Enter any statement and instantly see its emotional analysis, powered by IBM Watson NLP.

Features
🎨 Cyberpunk dark mode with animated neon gradient UI.

⏳ Animated loading spinner to indicate real-time analysis.

🧠 AI-powered emotion detection via IBM Watson EmotionPredict API.

✅ Intuitive web UI and RESTful API endpoint.

🛡️ Network timeout handling with demo fallback results for offline use.

🔬 Unit tests for guaranteed correctness.

📱 Responsive, mobile-ready design.

Demo
Input:
I think I am having fun!

Output:

For the given statement, the system response is 'anger': 0.1, 'disgust': 0.05, 'fear': 0.05, 'joy': 0.8, and 'sadness': 0.0.
The dominant emotion is joy.

Prerequisites
Python 3.9+

Internet access for live Watson API (offline mode provides fallback demo analysis)

Git

Quick Start
Clone the repository

git clone https://github.com/YOURUSERNAME/AI-Emotion-Detection-Web-App-IBM-Skills-Network-.git
cd AI-Emotion-Detection-Web-App-IBM-Skills-Network-

(Optional) Create and activate a virtual environment

python3 -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows (Powershell)
.venv\Scripts\Activate.ps1

Install dependencies

python3 -m pip install --upgrade pip
python3 -m pip install flask requests pylint

Run unit tests (recommended)

python3 -m unittest final_project/test_emotion_detection.py

Launch the web app

python3 final_project/server.py

Open the UI

Go to http://localhost:5000 in your web browser.

Enter any sentence (e.g., I think I am having fun) and click "Analyze Emotions".

The result will display below with emotion scores and dominant emotion.

Submitting an empty input returns: Invalid text! Please try again!

API Usage
Endpoint:
POST http://localhost:5000/emotionDetector

Send either:

Form-encoded body: textToAnalyze=Your text here

JSON: {"textToAnalyze": "Your text here"}

Example cURL:

bash
curl -X POST -F "textToAnalyze=I think I am having fun" http://localhost:5000/emotionDetector
Response:

On success: a plain-text sentence with anger, disgust, fear, joy, sadness scores and the dominant emotion.

On invalid/blank: "Invalid text! Please try again!"

Customization
UI Theme: All CSS and design in templates/index.html.

Backend logic: All emotion detection in final_project/EmotionDetection/emotion_detection.py.

Tests: Update or expand tests in final_project/test_emotion_detection.py.

Notes
Do not move templates/ or static/; the server expects them at the repository root.

The app calls IBM’s Watson EmotionPredict endpoint. If the API is down or blocked, the app uses fallback local analysis logic so the UI always works.

Credits
Project based on the IBM Skills Network
Extended with a custom cyberpunk UI and enhanced error handling by Arees Manesia.

Ready to use! Check out the code, launch the server, and experience advanced emotion detection with cutting-edge design.
