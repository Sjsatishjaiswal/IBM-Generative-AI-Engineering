Emotion Detection Application
Project Description

This project is an Emotion Detection Application developed using Python, Flask, and the Watson NLP Emotion Prediction service.

The application analyzes a user-provided statement and identifies five emotions:

Anger

Disgust

Fear

Joy

Sadness

It also determines the dominant emotion in the statement.

Project Structure
IBM-Generative-AI-Engineering/
├── README.md
├── requirements.txt
├── server.py
├── test_emotion_detection.py
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
└── templates/
    └── index.html

Features

Emotion detection using Watson NLP.

Flask web application.

Formatted emotion scores.

Dominant emotion detection.

Error handling for blank input.

HTTP 400 error handling.

Unit testing using Python unittest.

Static code analysis using Pylint.

Running the Application

Install the required packages:

pip install -r requirements.txt


Run the Flask application:

python server.py


The application runs on port 5000.

Open the application in a browser and enter a statement to analyze.

Unit Testing

Run:

python -m unittest test_emotion_detection.py


The expected result is:

.....
Ran 5 tests
OK

Static Code Analysis

Run:

pylint server.py


The project should achieve a Pylint score of:

Your code has been rated at 10.00/10

Example

Input:

I am very happy today!


Example result:

For the given statement, the system response is:
anger: 0.001,
disgust: 0.001,
fear: 0.001,
joy: 0.98 and
sadness: 0.001.
The dominant emotion is joy.
