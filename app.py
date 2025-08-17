from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# جلب الـ API key من متغير البيئة
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def home():
    return "Hello from Flask + OpenAI!"

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("question", "")
    
    if not question:
        return jsonify({"error": "No question provided"}), 400

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": question}]
        )
        answer = response["choices"][0]["message"]["content"]
        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
