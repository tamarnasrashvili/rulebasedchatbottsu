from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import pandas as pd

app = Flask(__name__)

ENV = 'DEV'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

if ENV == 'DEV':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Admin123@postgres/chatbotdb'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

db = SQLAlchemy(app)


class Question(db.Model):
    __tablename__ = 'Question'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(1000))
    answer = db.Column(db.String(5000))

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


db = SQLAlchemy(app)


def insert_qa():
    df = pd.read_excel("app/dummy_data.xlsx")
    question = ""
    answer = ""

    questions = df["QUESTION"].tolist()
    answers = df["ANSWER"].tolist()
    excelCount = 0
    insertedCount = 0
    for (questionIter, answerIter) in zip(questions, answers):
        excelCount = excelCount + 1
        question = questionIter
        answer = answerIter
        if not db.session.query(Question.id).filter_by(question=question).first():
            questionRow = Question(question, answer)
            db.session.add(questionRow)
            db.session.commit()
            insertedCount = insertedCount + 1
    return excelCount, insertedCount


db.create_all()

migrate = Migrate(app, db)
manager = Manager(app)


insert_qa()

