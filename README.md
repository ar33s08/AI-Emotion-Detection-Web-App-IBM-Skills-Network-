# Repository for final project
Prerequisites
Python 3.9+ installed.

Internet access (the app calls the Watson EmotionPredict endpoint).

1) Clone the repository
git clone https://github.com/<your-username>/AI-Emotion-Detection-Web-App-IBM-Skills-Network-.git

cd AI-Emotion-Detection-Web-App-IBM-Skills-Network-

2) (Optional) Create and activate a virtual environment
python3 -m venv .venv

macOS/Linux: source .venv/bin/activate

Windows (PowerShell): .venv\Scripts\Activate.ps1

3) Install dependencies
python3 -m pip install --upgrade pip

python3 -m pip install flask requests pylint

4) Quick function smoke test (optional)
python3

from EmotionDetection import emotion_detector

emotion_detector("I love this new technology.")

exit()

Expected: a dict with scores for anger, disgust, fear, joy, sadness, and a dominant_emotion key.

5) Run unit tests (optional but recommended)
python3 -m unittest final_project/test_emotion_detection.py

Expected: all tests pass, validating dominant_emotion for five sample statements.

6) Launch the web app
python3 final_project/server.py

Server starts at:

http://localhost:5000

7) Use the UI
Open the URL in a browser, enter any sentence (e.g., “I think I am having fun”), and submit.

The page returns a formatted sentence containing the five emotion scores and the dominant emotion.

Submitting an empty/blank input returns: “Invalid text! Please try again!”

8) API usage (direct, without the UI)
Endpoint:

POST http://localhost:5000/emotionDetector

Send either:

Form-encoded body with key textToAnalyze

or JSON body: {"textToAnalyze": "Your text here"}

Response:

On success: a plain-text sentence with 'anger', 'disgust', 'fear', 'joy', 'sadness' and the dominant emotion.

On invalid/blank text: “Invalid text! Please try again!”

cURL examples:

curl -X POST -F "textToAnalyze=I think I am having fun" http://localhost:5000/emotionDetector

curl -X POST -H "Content-Type: application/json" -d '{"textToAnalyze":"I think I am having fun"}' http://localhost:5000/emotionDetector

9) Linting (optional)
python3 -m pylint final_project/server.py

Aim for 10/10 by keeping docstrings and type hints; repeat for other files if desired.

Notes
Do not move templates/ or static/; the server expects them at the repository root.

The app calls IBM’s Watson EmotionPredict endpoint specified in the lab; ensure the network allows outgoing HTTPS requests.

