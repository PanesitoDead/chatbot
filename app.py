from flask import Flask, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Configura tu API key de Gemini
genai.configure(api_key="AIzaSyDcnHrEgO6HqSIHfH0Lv82LO1rIoqGkZFI")

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message')
    if not message:
        return jsonify({'error': 'Mensaje requerido'}), 400

    # Llama a Gemini
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(message)
    return jsonify({'response': response.text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)