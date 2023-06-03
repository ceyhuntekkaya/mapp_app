from db import db


class CommandCollarMarkRankModel(db.Model):
    __tablename__ = "command_collar_mark_rakss"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    hierarchical_order = db.Column(db.Integer, unique=True, nullable=False)
    command_collar_mark_id = db.Column(
        db.Integer, db.ForeignKey("command_collar_marks.id"), unique=False, nullable=False
    )