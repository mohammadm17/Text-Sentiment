from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import joblib

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sentiment_data.db'  # SQLite database
db = SQLAlchemy(app)

class SentimentData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text_input = db.Column(db.String(500), nullable=False)
    predicted_sentiment = db.Column(db.Integer, nullable=True)

# Loading  the saved model from the file
loaded_model = joblib.load(r'C:\Users\Kashmeen\Downloads\random_forest_model.pkl')

SENTIMENT_LABELS = {0: 'Negative', 1: 'Positive'}


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    text_input = request.form['text_input']

    # Make predictions on the custom text input
    predicted_sentiment = loaded_model.predict([text_input])[0]

    sentiment_label = SENTIMENT_LABELS.get(predicted_sentiment, 'Unknown')

    # Log the input to a log file
    with open('sentiment_predictions.log', 'a') as log_file:
        log_line = f'Text: {text_input} | Predicted Sentiment: {predicted_sentiment}\n'
        log_file.write(log_line)

    # Store input and output in the SQL database
    sentiment_data = SentimentData(text_input=text_input, predicted_sentiment=sentiment_label)
    db.session.add(sentiment_data)
    db.session.commit()

    return render_template('result.html', text_input=text_input, predicted_sentiment=sentiment_label)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

