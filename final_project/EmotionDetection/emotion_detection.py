"""
Emotion detection client for Watson NLP EmotionPredict.
Provides emotion_detector(text) that returns scores and dominant_emotion.
"""

from __future__ import annotations
from typing import Dict, Optional
import json
import requests

WATSON_EMOTION_URL = (
    "https://sn-watson-emotion.labs.skills.network/v1/"
    "watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
WATSON_HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}


def _format_response(payload: dict) -> Dict[str, Optional[float]]:
    """
    Convert Watson payload to required dict with dominant_emotion.
    If payload is missing or malformed, return None values per spec.
    """
    result: Dict[str, Optional[float]] = {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None,
    }

    try:
        predictions = payload.get("emotionPredictions", [])
        if not predictions:
            return result

        emotions = predictions.get("emotion", {})
        for key in ("anger", "disgust", "fear", "joy", "sadness"):
            if key in emotions:
                result[key] = float(emotions[key])

        scored = {
            k: v for k, v in result.items()
            if k != "dominant_emotion" and isinstance(v, float)
        }
        if scored:
            result["dominant_emotion"] = max(scored, key=scored.get)
    except Exception:
        # On unexpected schema, return None values (keeps behavior consistent)
        return result

    return result


def emotion_detector(text_to_analyze: str) -> Dict[str, Optional[float]]:
    """
    Call Watson EmotionPredict and return dict with five emotions + dominant_emotion.
    On HTTP 400 (e.g., blank input), return dict with all values None as per spec.
    """
    if text_to_analyze is None:
        text_to_analyze = ""

    payload = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(
        WATSON_EMOTION_URL,
        headers=WATSON_HEADERS,
        json=payload,
        timeout=15
    )

    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    response.raise_for_status()
    data = json.loads(response.text)
    return _format_response(data)

