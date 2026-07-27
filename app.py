from flask import Flask, request, jsonify

from database import db
from models import Note

app = Flask(__name__)

import os

app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"postgresql://"
    f"{os.getenv('DB_USER')}:"
    f"{os.getenv('DB_PASSWORD')}@"
    f"{os.getenv('DB_HOST')}/"
    f"{os.getenv('DB_NAME')}"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return {"message": "Secure Notes API"}


@app.route("/notes", methods=["POST"])
def create_note():

    data = request.get_json()

    note = Note(content=data["content"])

    db.session.add(note)
    db.session.commit()

    return jsonify(note.to_dict()), 201


@app.route("/notes", methods=["GET"])
def get_notes():

    notes = Note.query.all()

    return jsonify([note.to_dict() for note in notes])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)