from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Define the Chatbot's Responses
responses = [
    "Hello! How can I help you today?",
    "What's on your mind?",
    "I'm here to assist you. What do you need?",
    "How can I assist you?",
    "What can I help you with?",
]

# Implement the Chatbot's Response Function
def chatbot_response(user_input):
    user_input = user_input.lower()
    if "movie" in user_input:
        return "I recommend checking out the IMDb website for movie recommendations. They have a wide variety of genres and ratings to choose from."
    elif "weather" in user_input:
        return "You can check the weather by using a weather website or app. Some popular ones include Weather.com and The Weather Channel app."
    elif "news" in user_input:
        return "There are many websites and apps that offer the latest news updates, such as CNN, Fox News, and NBC News."
    elif "joke" in user_input:
        return "Why couldn't the bicycle stand up by itself? Because it was two-tired!"
    else:
        return responses[0]  # Default response if no condition is met

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send():
    user_input = request.get_json()['userInput']
    response = chatbot_response(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
