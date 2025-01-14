from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Configure OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/generate", methods=["POST"])
def generate_content():
    data = request.json
    prompt = data.get("prompt", "")
    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=100,
        )
        return jsonify({"content": response.choices[0].text.strip()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
