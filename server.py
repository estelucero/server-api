from flask import Flask, jsonify, request
from chatbot import answer_message

app = Flask(__name__)

@app.route('/api/chatbot', methods=['POST'])
def chatbot():
    data = request.get_json()
    user_message = data['message']
    bot_response = answer_message(user_message)
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)