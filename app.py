"""
Flask backend application for CI/CD pipeline demonstration
"""
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    """Home endpoint returning a simple message"""
    return jsonify({
        "status": "success",
        "message": "CI/CD Pipeline is working!",
        "code": 200
    })


@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "version": "1.0.0"
    })


@app.route('/api/add', methods=['GET'])
def add_numbers():
    """Test endpoint that adds two numbers"""
    result = 1 + 1
    return jsonify({
        "operation": "add",
        "operand1": 1,
        "operand2": 1,
        "result": result
    })


if __name__ == '__main__':
    app.run(debug=True, port=5000)
