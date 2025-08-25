"""
Flask web server for Emotion Detection app using Watson NLP.
Serves the provided index.html and exposes /emotionDetector.
"""

from __future__ import annotations
import os
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from typing import Any, Dict
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

# Tell Flask where templates and static files are (at repo root, not relative to server.py)
app = Flask(__name__, 
            template_folder=os.path.join(REPO_ROOT, 'templates'),
            static_folder=os.path.join(REPO_ROOT, 'static'))


@app.route("/")
def index() -> Any:
    """Render the provided index.html UI."""
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET", "POST"])
def detect_emotion() -> Any:
    """
    Receive text via JSON, form, or GET query and return formatted emotion analysis.
    """
    text = ""
    
    if request.method == "GET":
        # Handle GET request from the IBM JavaScript
        text = (request.args.get("textToAnalyze") or "").strip()
    elif request.is_json:
        # Handle JSON POST
        data = request.get_json(silent=True) or {}
        text = (data.get("textToAnalyze") or "").strip()
    else:
        # Handle form POST
        text = (request.form.get("textToAnalyze") or "").strip()

    result: Dict[str, Any] = emotion_detector(text)

    if result.get("dominant_emotion") is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {result.get('anger')}, "
        f"'disgust': {result.get('disgust')}, "
        f"'fear': {result.get('fear')}, "
        f"'joy': {result.get('joy')}, "
        f"and 'sadness': {result.get('sadness')}. "
        f"The dominant emotion is {result.get('dominant_emotion')}."
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
