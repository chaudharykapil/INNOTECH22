from extensions import db
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
    

class Manager(db.Model):
    id = db.Column(db.Integer,  primary_key=True)
    Longitude = db.Column(db.String(50), nullable=False,)
    Latitude= db.Column(db.String(50), nullable=False)
    time = db.Column(db.String(150),nullable=False)
    name=db.Column(db.String(500),nullable=False)

    def __repr__(self) -> str:
        return f"{self.id} - {self.name}"


