from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def call_detector():

    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)
    
    if result['dominant_emotion'] == None:
        return "Invalid text! Please try again!"
        
    else:
        return f"For the given statement, the system response is 'anger': {result['anger']}, 'disgust': {result['disgust']}, 'fear': {result['fear']}, \
        'joy': {result['joy']} and 'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."

@app.route("/")
def index_():
    return render_template ("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)