import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load Dataset
df = pd.read_csv("ml/dataset/UpdatedResumeDataSet.csv")

# Features and Labels
X = df["Resume"]
y = df["Category"]

# Convert Text to Numbers
vectorizer = TfidfVectorizer(stop_words="english")

X_vectorized = vectorizer.fit_transform(X)

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized,
    y,
    test_size=0.2,
    random_state=42
)

# Train Model
model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print(f"Accuracy : {accuracy * 100:.2f}%")

# Save Model
joblib.dump(model, "ml/models/model.pkl")

# Save Vectorizer
joblib.dump(vectorizer, "ml/models/vectorizer.pkl")

print("Model Saved Successfully!")