"""
This is a Flask server for the Emotion Detection application.
It provides a web interface to analyze text for emotions.
"""
from flask import Flask, render_template, request
from Emotiondetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector") # pylint: disable=invalid-name


@app.route('/emotionDetector')
def emo_detect():
    """
    Handles the emotion detection logic by taking text input
    from a URL query parameter and returning the analysis.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is <b>{response['dominant_emotion']}</b>."
    )
    return formatted_response


@app.route("/")
def render_index_page():
    """
    Renders the main HTML page for the application.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
