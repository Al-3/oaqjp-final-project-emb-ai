"""
This is a simple Flask-based web server that detectis emotions in text.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    """
    Function to run emotion_detector() using user input
    """

    text_to_detect = request.args.get("textToAnalyze")

    response = emotion_detector(text_to_detect)

    anger_score = response["anger"]
    disgust_score = response["disgust"]
    fear_score = response["fear"]
    joy_score = response["joy"]
    sadness_score = response["sadness"]
    dominant_emotion = response["dominant_emotion"]

    if dominant_emotion is None:

        return "Invalid text! Please try again!."

    return (f"For the given statement, the system response is"
            f" 'anger': {anger_score}, 'disgust': {disgust_score}, 'fear': {fear_score}"
            f", 'joy': {joy_score} and 'sadness': {sadness_score}."
            f" The dominant emotion is {dominant_emotion}.")

@app.route("/")
def render_index_page():
    """
    Function to render the index page
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
