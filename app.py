# app.py

from flask import Flask, render_template, request, redirect, url_for, jsonify
from datetime import datetime

app = Flask(__name__)

# Store the list of users in a dictionary
users = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    username = request.form['username']
    users[username] = request.remote_addr
    return render_template('chat.html', username=username, users=users)

@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.form['message']
    sender = request.form['sender']
    recipient = request.form['recipient']
    timestamp = datetime.now().strftime("%H:%M:%S")
    return {'message': message, 'sender': sender, 'recipient': recipient, 'timestamp': timestamp}

@app.route('/user_list')
def user_list():
    return jsonify(list(users.keys()))

if __name__ == '__main__':
    app.run(debug=True)
