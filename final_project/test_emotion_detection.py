"""
Unit tests for emotion_detector covering five canonical statements and dominant emotions.
"""

import os
import sys

# Add the repo root to Python path - go up two levels from this file
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO_ROOT)

import unittest
from EmotionDetection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """Tests for the dominant_emotion field over sample inputs."""

    def test_joy(self):
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result.get("dominant_emotion"), "joy")

    def test_anger(self):
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result.get("dominant_emotion"), "anger")

    def test_disgust(self):
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result.get("dominant_emotion"), "disgust")

    def test_sadness(self):
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result.get("dominant_emotion"), "sadness")

    def test_fear(self):
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result.get("dominant_emotion"), "fear")


if __name__ == "__main__":
    unittest.main()
