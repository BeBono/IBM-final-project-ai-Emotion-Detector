from EmotionDetection.emotion_detection import emotion_detector
import unittest


class UnitTesting(unittest.TestCase):
    def test_emotion(self):
        anger = emotion_detector("I am really mad about this")
        disgust = emotion_detector("I feel disgusted just hearing about this")
        fear = emotion_detector("I am really afraid that this will happen")
        joy = emotion_detector("I am glad this happened")
        sadness = emotion_detector("I am so sad about this")

        self.assertEqual(anger['dominant_emotion'], "anger")
        self.assertEqual(disgust['dominant_emotion'], "disgust")
        self.assertEqual(fear['dominant_emotion'], "fear")
        self.assertEqual(joy['dominant_emotion'], "joy")
        self.assertEqual(sadness['dominant_emotion'], "sadness")
        
unittest.main()




