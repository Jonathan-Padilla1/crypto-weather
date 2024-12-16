from enum import unique
from app import db
# user forgien key to define data relations
##collaborator_user_id = Column(Integer, ForeignKey("collaborators.user_id"), nullable=False)


class User(db.Model):
    __tablename__ = "user" # defines the table name

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(80), nullable=False, unique=True)

    # debugging 
    def __repr__(self):
        return f"<User {self.name}>"

