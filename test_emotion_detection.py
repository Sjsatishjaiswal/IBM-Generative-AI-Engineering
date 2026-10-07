import unittest

from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):

    def test_joy(self):
        result = emotion_detector("I am glad this happened")
        self.assertIsNotNone(result)
        self.assertIn("joy", result)
        self.assertEqual(result["dominant_emotion"], "joy")

    def test_anger(self):
        result = emotion_detector("I am very angry about this")
        self.assertIsNotNone(result)
        self.assertIn("anger", result)
        self.assertEqual(result["dominant_emotion"], "anger")

    def test_disgust(self):
        result = emotion_detector("This is disgusting")
        self.assertIsNotNone(result)
        self.assertIn("disgust", result)
        self.assertEqual(result["dominant_emotion"], "disgust")

    def test_sadness(self):
        result = emotion_detector("I am feeling very sad")
        self.assertIsNotNone(result)
        self.assertIn("sadness", result)
        self.assertEqual(result["dominant_emotion"], "sadness")

    def test_fear(self):
        result = emotion_detector("I am afraid of this")
        self.assertIsNotNone(result)
        self.assertIn("fear", result)
        self.assertEqual(result["dominant_emotion"], "fear")


if __name__ == "__main__":
    unittest.main()
