import joblib

# Load saved model and vectorizer
model = joblib.load('model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

# Input sample email content
with open('sample_input.txt', 'r') as file:
    email_text = file.read()

# Transform input and predict
email_vector = vectorizer.transform([email_text])
prediction = model.predict(email_vector)[0]

# Output result
print("\nPrediction Result:")
print("🔒 Fraudulent Email" if prediction == 1 else "✅ Legitimate Email")
