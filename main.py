from flask import Flask, jsonify, request
import random
import json
app = Flask(__name__)
@app.route('/jokes/', methods=['GET', 'POST'])

def joke():

    args = request.args
    num = args.get(random.randint(1,10))

    jokes = [
        "What does a house wear? Address!",
        "How does NASA organize a party? They planet.",
        "What gets wetter the more it dries? A towel.",
        "Want to hear a joke about a roof? The first one’s on the house.",
        "Why dont blind people skydive? Because it scares their dogs.",
        "I tried to win a suntanning competition. But all I got was bronze.",
        "Why are crabs so bad at sharing? Because they’re all shellfish.",
        "How do you make a tissue dance? Put a little boogie in it.",
        "What kind of shoes does a spy wear? Sneakers.",
        "Why are frogs always so happy? They eat whatever bugs them."
    ]

    return jsonify(
        jokes = random.sample(jokes,num)
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)