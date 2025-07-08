# Fraud-Email-Detection
Fraud Email Detection System

This project implements a machine learning-based system to detect fraudulent emails. Using text preprocessing, feature extraction, and classification techniques, the system achieves high accuracy in distinguishing between legitimate and fraudulent emails.

---
*Features*

Preprocesses email text data to remove noise.

Uses TF-IDF Vectorization for feature extraction.

Employs a Random Forest Classifier for robust classification.

Evaluates model performance using metrics like accuracy, classification report, and confusion matrix.

---
*Dataset*

The model requires a dataset in CSV format with the following columns:

Text: Contains the email content.

Class: Labels indicating whether the email is fraudulent (e.g., 1) or legitimate (e.g., 0).

---

*Requirements*

The following Python libraries are required to run the project:

pandas

scikit-learn


Install the dependencies using pip:

pip install pandas scikit-learn

How It Works

1. Data Loading and Preprocessing:

Loads the dataset from a CSV file.

Removes rows with missing email content.



2. Text Vectorization:

Converts email content into numerical features using TF-IDF Vectorization.



3. Model Training:

Trains a Random Forest Classifier on the preprocessed data.



4. Model Evaluation:

Evaluates the classifier's performance using accuracy, classification report, and confusion matrix.

---
*Results*

The model outputs the following:

1. Accuracy: Measures the overall performance of the classifier.


2. Classification Report: Provides precision, recall, and F1-score for each class.


3. Confusion Matrix: Summarizes the classification results in a matrix format.



Output

Accuracy: 0.9891

Classification Report:
               precision    recall  f1-score   support

           0       0.99      0.99      0.99      1349
           1       0.99      0.98      0.99      1037

    accuracy                           0.99      2386
   macro avg       0.99      0.99      0.99      2386
weighted avg       0.99      0.99      0.99      2386

Confusion Matrix:
 [[1340    9]
 [  17 1020]]

---
*Contribution*

Feel free to fork this repository and improve the code. Pull requests are welcome!

License

This project is licensed under the MIT License.


---
