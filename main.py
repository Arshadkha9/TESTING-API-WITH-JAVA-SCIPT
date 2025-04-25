from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow requests from JS frontend

@app.route('/login', methods=['GET', 'POST'])
def login():
    print("hii")
    
    return jsonify({"message": "Hello from Flask!"})

@app.route('/api/echo', methods=['POST'])
def echo():
    data = request.get_json()
    return jsonify({"you_sent": data})

if __name__ == '__main__':
    app.run(debug=True) 
