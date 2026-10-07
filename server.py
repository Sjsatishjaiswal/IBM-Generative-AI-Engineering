from flask import Flask, request, render_template

from EmotionDetection.emotion_detection import emotion_detector


app = Flask(__name__)


@app.route("/")
def render_index_page():
    """Render the main web page."""
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_route():
    """Detect emotions from user input."""

    text_to_analyze = request.args.get("textToAnalyze")

    if not text_to_analyze or not text_to_analyze.strip():
        return "Invalid input! Try again."

    response = emotion_detector(text_to_analyze)

    if response is None or response["dominant_emotion"] is None:
        return "Invalid input! Try again."

    return (
        "For the given statement, the system response is: "
        f"anger: {response['anger']}, "
        f"disgust: {response['disgust']}, "
        f"fear: {response['fear']}, "
        f"joy: {response['joy']} and "
        f"sadness: {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
