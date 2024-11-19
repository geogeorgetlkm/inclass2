from flask import Flask, jsonify, request

app = Flask(__name__)


# Utility Functions
def calculate_sum(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Inputs must be numbers.")
    return a + b


def get_status():
    return "healthy"


# Routes
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Flask App!"}), 200


@app.route("/api/data", methods=["POST"])
def api_data():
    data = request.get_json()
    if "a" not in data or "b" not in data:
        return jsonify({"error": "Invalid input"}), 400

    result = calculate_sum(data["a"], data["b"])
    return jsonify({"result": result}), 200


@app.route("/api/status", methods=["GET"])
def api_status():
    return jsonify({"status": get_status()}), 200


# Main entry point
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
