from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("mysql+mysqlconnector://root:root@localhost:3306/finances-project-test")
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

db = SQLAlchemy()


def save(model: db.Model):
    session.add(model)
    commit()
    return model


def commit():
    session.commit()
