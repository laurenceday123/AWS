from flask import Flask, request
import joblib 

vectorizer = joblib.load("vectorizer.pkl")
model = joblib.load("spam_detector.pkl")

application = Flask(__name__)

@application.route('/')
def home():
    return "Homepage for Spam Detection ML Model"

@application.route('/spam', methods=['GET', 'POST'])
def spam():
    message = request.args.get("message")
    vect_message = vectorizer.transform([message])
    result = model.predict(vect_message)[0]
    return result 


if __name__ == "__main__":
    application.run()