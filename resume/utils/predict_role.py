import joblib
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

model = joblib.load(os.path.join(BASE_DIR, "ml", "models", "model.pkl"))
vectorizer = joblib.load(os.path.join(BASE_DIR, "ml", "models", "vectorizer.pkl"))


def predict_role(text):

    text_vector = vectorizer.transform([text])

    prediction = model.predict(text_vector)

    return prediction[0]