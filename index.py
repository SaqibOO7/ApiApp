from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains

# Load JSON data
with open("q-vercel-python.json", "r") as f:
    students = json.load(f)

@app.route("/api", methods=["GET"])
def get_marks():
    names = request.args.getlist("name")  # Get list of names from query
    marks = [next((s["marks"] for s in students if s["name"] == name), None) for name in names]
    return jsonify({"marks": marks})

# Vercel requires `app` to be callable
if __name__ == "__main__":
    app.run(debug=True)
