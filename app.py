from flask import Flask, request, jsonify
import os

from database import db
from models import Note

app = Flask(__name__)

# Database configuration
DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL:
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
else:
    # Used for local testing and GitHub Actions
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

# Create database tables
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return jsonify({"message": "Secure Notes API"})


@app.route("/notes", methods=["POST"])
def create_note():
    data = request.get_json()

    if not data or "content" not in data:
        return jsonify({"error": "Content is required"}), 400

    note = Note(content=data["content"])

    db.session.add(note)
    db.session.commit()

    return jsonify(note.to_dict()), 201


@app.route("/notes", methods=["GET"])
def get_notes():
    notes = Note.query.all()
    return jsonify([note.to_dict() for note in notes])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)