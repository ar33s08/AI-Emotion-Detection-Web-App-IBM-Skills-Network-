"""
Flask web server for Emotion Detection app using Watson NLP.
Serves the provided index.html and exposes /emotionDetector.
"""

from __future__ import annotations
from typing import Any, Dict
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index() -> Any:
    """Render the provided index.html UI."""
    return render_template("index.html")


@app.route("/emotionDetector", methods=["POST"])
def detect_emotion() -> Any:
    """
    Receive text via JSON or form, call emotion_detector, and return the formatted string.
    On invalid/blank input (dominant_emotion is None), return the required error message.
    """
    text = ""
    if request.is_json:
        data = request.get_json(silent=True) or {}
        text = (data.get("textToAnalyze") or "").strip()
    else:
        text = (request.form.get("textToAnalyze") or "").strip()

    result: Dict[str, Any] = emotion_detector(text)

    if result.get("dominant_emotion") is None:
        return "Invalid text! Please try again!"

    # Specified response sentence format
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
    # Must run on localhost:5000 per the lab
    app.run(host="127.0.0.1", port=5000, debug=False)

