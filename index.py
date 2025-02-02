from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)  # Enable CORS

# Load the data from the JSON file
with open("q-vercel-python.json") as f:
    data = json.load(f)

@app.route("/api", methods=["GET"])
def get_marks():
    names = request.args.getlist("name")  # Get multiple 'name' params
    marks = [student["marks"] for student in data if student["name"] in names]
    return jsonify({"marks": marks})

# Only needed for local testing
if __name__ == "__main__":
    app.run(debug=True)
