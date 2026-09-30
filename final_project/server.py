"""
Executing this module initiates the application of emotion detection
to be executed over the Flask server.
"""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

# Initialize the Flask application
app = Flask(__name__)


@app.route("/")
def render_index_page():
    """Renders the main index application page template interface."""
    return render_template("index.html")


@app.route("/emotionDetector")
def detect_emotion():
    """Retrieves text from the request arguments, passes it to the detector

    module, and returns the formatted analytical system response string.
    Handles blank inputs or invalid queries by validating the dominant emotion.
    """
    # Retrieve the text input from the incoming request parameters
    text_to_analyze = request.args.get("textToAnalyze")

    # Pass the text to the packaged emotion detector application function
    response = emotion_detector(text_to_analyze)

    # Extract individual parameters from the returned response dictionary
    anger = response["anger"]
    disgust = response["disgust"]
    fear = response["fear"]
    joy = response["joy"]
    sadness = response["sadness"]
    dominant_emotion = response["dominant_emotion"]

    # If dominant_emotion evaluates to None, return the error message string
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    # Construct the exact output display string pattern requested by the customer
    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )


if __name__ == "__main__":
    # Deploy the application to execute on localhost:5000
    app.run(host="0.0.0.0", port=5000)
