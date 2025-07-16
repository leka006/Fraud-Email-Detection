Fraud Email Detection
This project uses machine learning to detect whether an email is fraudulent or legitimate. It trains a Random Forest model using TF-IDF features from email content.

What It Does
Cleans and prepares email text data.
Converts text into numbers using TF-IDF vectorizer.
Trains a Random Forest classifier.
Can predict if a new email is a fraud or not.
Files in the Project
train_email_detector.py – Trains the model and saves it.
predict_email.py – Predicts fraud using saved model.
model.pkl – The trained model file.
vectorizer.pkl – TF-IDF vectorizer file.
sample_input.txt – Text file containing sample email for testing.
requirements.txt – List of required libraries.
How to Use
1. Install Dependencies
pip install -r requirements.txt

2. Train the Model
python train_email_detector.py

3.Predict for New mail
python predict_email.py 
