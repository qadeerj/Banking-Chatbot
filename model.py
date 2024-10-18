import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Step 1: Load the dataset
data = pd.read_csv(r'C:\Users\muham\Desktop\Datascience projects\NLP_Projects\Chatbot\BankFAQs.csv')

# Step 2: Split the dataset into features (questions) and target (answers)
X = data['Question']  # Questions
y = data['Answer']    # Direct answers

# Step 3: Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Text Vectorization and Model Training (Pipeline)
model = make_pipeline(TfidfVectorizer(), RandomForestClassifier())

# Step 5: Train the model
model.fit(X_train, y_train)

# Step 6: Test the model and get predictions
y_pred = model.predict(X_test)

# Step 7: Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")

# Optional: Display detailed classification report
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

# Step 8: Save the trained model
joblib.dump(model, 'chatbot_model.pkl')
