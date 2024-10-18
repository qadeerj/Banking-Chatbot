from flask import Flask,render_template, request, jsonify
import joblib

# Step 1: Initialize the Flask app
app = Flask(__name__)

# Step 2: Load the pre-trained model
model = joblib.load('chatbot_model.pkl')

# Step 3: Define a function to handle greetings
def get_greeting_response(user_input):
    greetings = {
        "hello": "Hi there! How can I assist you today?",
        "hi": "Hello! What can I help you with?",
        "hey": "Hey! How's it going?",
        "good morning": "Good morning! How can I help you today?",
        "good evening": "Good evening! What can I assist you with?",
        "good afternoon": "Good afternoon! How can I help you today?",
        "how are you": "I'm just a chatbot, but thanks for asking! How can I assist you?",
        "how's it going": "It's going well, thanks for asking! How can I help?",
        "whats up": "Not much! How about you? How can I assist you?",
        "what's happening": "I'm here to help! What's happening with you?",
        "hi there": "Hi there! How can I help?",
        "greetings": "Greetings! How may I assist you?",
        "hello there": "Hello there! What can I do for you today?",
        "hey there": "Hey there! How can I assist you?",
        "good day": "Good day! How can I help you today?",
        "good time": "Good time! What can I assist you with?",
        "good luck": "Good luck! How can I help you today?",
        "good luck with that": "Good luck with that! How can I assist you?",
        "good luck with everything": "Good luck with everything! How can I help you today?",
        "good luck with your day": "Good luck with your day! How can I assist you",
        "what is your name": "I'm a chatbot, and I don't have a real name, but you can call me Chatbot! What's your name?",
        "who are you": "I'm a helpful chatbot here to assist you!",
        "what's your name": "I go by Chatbot! How can I assist you today?",
        "how old are you": "I'm timeless! But I'm always ready to help you.",
        "your age": "Age doesn't really apply to chatbots, but I've been learning since I was created!",
        "thank you": "You're welcome! I'm happy to help.",
        "thanks": "You're welcome! Let me know if you need anything else.",
        "thank you so much": "My pleasure! Feel free to ask me anything.",
        "thanks a lot": "You're very welcome! I'm here if you need more assistance.",
        "thank you chatbot": "You're welcome! I'm glad I could assist you!"
    
    }
    
    # Normalize user input to lowercase
    user_input = user_input.lower()
    
    # Return the corresponding greeting response if it matches
    return greetings.get(user_input, None)

# Step 4: Route to render the chatbot interface
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# Step 5: Route to handle user input and predict the answer
@app.route('/chatbot', methods=['GET'])
def chatbot():
    user_input = request.args.get('question')
    
    if not user_input:
        return jsonify({"answer": "Please provide a question."}), 400

    # Step 6: Check for greetings
    greeting_response = get_greeting_response(user_input)
    if greeting_response:
        return jsonify({"answer": greeting_response})
    
    # Step 7: Predict the answer based on the user's question
    predicted_answer = model.predict([user_input])[0]
    
    return jsonify({"answer": predicted_answer})

# Step 8: Run the app
if __name__ == '__main__':
    app.run(debug=True)
