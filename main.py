import os
from flask import Flask, render_template, request, jsonify
from groq import Groq

app = Flask(__name__)

# Initialize Groq API client
client = Groq(api_key="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")

def get_groq_response(topic, days):
    """Fetches curriculum from Groq API based on user input."""
    try:
        prompt = f"Create a {days}-day curriculum for learning {topic}."
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/')
def index():
    """Renders the main webpage."""
    return render_template('index.html')

@app.route('/get_curriculum', methods=['POST'])
def get_curriculum():
    """Handles AJAX request for curriculum generation."""
    data = request.json
    topic = data.get("topic")
    days = data.get("days")

    if not topic or not days:
        return jsonify({"error": "Please provide both a topic and number of days"}), 400

    curriculum = get_groq_response(topic, days)
    return jsonify({"curriculum": curriculum})

if __name__ == '__main__':
    app.run(debug=True)






'''
import os

from groq import Groq

client = Groq(
    api_key=os.environ.get("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"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "make a curriculam of learning quantum computing in 7 days",
        }
    ],
    model="llama-3.3-70b-versatile",
)

print(chat_completion.choices[0].message.content)
'''
#export GROQ_API_KEY=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
