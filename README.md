# Banking Chatbot

This project is a Banking Chatbot built using Flask, a pre-trained machine learning model for natural language processing, and a CSV dataset containing frequently asked banking questions and answers. The application allows users to interact with the chatbot and receive accurate answers based on their queries.

## Dataset
The dataset used in this project can be found in `BankFAQs.csv`. It contains pairs of banking-related questions and their corresponding answers.

## Model
The chatbot uses a machine-learning model built with the following components:

- **Random Forest Classifier:** An ensemble learning method that constructs multiple decision trees during training and outputs the mode of the classes (classification) of the individual trees.
- **TF-IDF Vectorization:** Converts the text data (user questions) into numerical form using the Term Frequency-Inverse Document Frequency (TF-IDF) method. This technique emphasizes words that are important in a particular document while downplaying common words.

### Implementation Steps
1. **Dataset Loading:** The model is trained using a dataset (`BankFAQs.csv`) containing pairs of banking-related questions and their corresponding answers.
2. **Data Preparation:** The dataset is split into features (questions) and target labels (answers). The data is further divided into training and testing sets using an 80-20 split.
3. **Pipeline Creation:** A machine learning pipeline is created that combines the TF-IDF vectorizer and the Random Forest Classifier.
4. **Model Training:** The model is trained on the training dataset.
5. **Model Evaluation:** The model is tested on the test dataset to obtain predictions. The accuracy of the model is calculated and printed, and a classification report is optionally displayed, showing precision, recall, and F1-score for each class.
6. **Model Saving:** The trained model is saved as `chatbot_model.pkl` for later use in the Flask application.

## Features
- User-friendly interface for interacting with the chatbot.
- Handles a variety of banking-related queries and provides relevant answers.
- Uses a machine learning model for accurate response generation.

## Technologies Used
- Flask: A lightweight WSGI web application framework in Python.
- scikit-learn: A machine learning library for Python.
- Pandas: For data manipulation and analysis.
- HTML/CSS: For the front-end design.

## Installation
### Prerequisites
- Python 3.x
- pip (Python package installer)

### Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/banking-chatbot.git
    cd banking-chatbot
    ```
2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
3. Prepare the dataset by ensuring that `BankFAQs.csv` is in the project root directory.
4. Run the application:
    ```bash
    python app.py
    ```
5. Open your browser and navigate to `http://127.0.0.1:5000/`.

## Contributing
Contributions are welcome! If you have suggestions for improvements or new features, please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
This project was developed as part of a personal initiative to create a functional banking chatbot. I want to give special thanks to the resources and tutorials that aided in its development.
