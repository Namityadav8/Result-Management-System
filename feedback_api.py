from flask import Flask, request, jsonify
import pymongo

app = Flask(__name__)
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["student_feedback"]
collection = db["feedback"]

@app.route("/feedback", methods=["POST"])
def feedback():
    data = request.json
    collection.insert_one(data)
    return jsonify({"message": "Feedback received"}), 200

if __name__ == "__main__":
    app.run(debug=True)