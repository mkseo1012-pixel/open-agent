import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/run', methods=['POST'])
def run_agent():
    api_key = request.json.get('api_key')
    if not api_key:
        return jsonify({'error': 'API key required'}), 400
    os.environ['API_KEY'] = api_key
    # Simple agent logic here
    return jsonify({'status': 'Agent running with provided key!', 'result': 'Hello from Open Agent!'})

if __name__ == '__main__':
    app.run(debug=True)
