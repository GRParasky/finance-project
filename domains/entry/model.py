from database import db, save, commit


class Entry(db.Model):
    __tablename__ = 'entry'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(500))
