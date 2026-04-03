from flask import Flask, render_template, request, jsonify
import wikipedia

app = Flask(__name__)

memory = []

triggers = [
    "tell me about", "who is", "what is", "explain", "information about"
]

def is_fact_query(msg):
    return any(trigger in msg.lower() for trigger in triggers)

def get_response(message):
    memory.append(message)

    if is_fact_query(message):
        try:
            result = wikipedia.summary(message, sentences=2)
            return result
        except:
            return "I couldn't find clear info. Try being more specific."

    elif "plan" in message.lower():
        return "Let's build a strong plan 🔥"

    elif "study" in message.lower():
        return "I'll teach you step-by-step 📘"

    elif "remember" in message.lower():
        return f"I remember {len(memory)} things about you 😉"

    else:
        return "Hmm... tell me more 🤔"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]
    reply = get_response(user_message)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)