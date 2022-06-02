from http.client import HTTPException
from urllib.error import HTTPError

from flask import request, jsonify, json

from app.similarity import get_similarity
from app.question_orm import get_questions_array, get_answer_by_question
from app import app, insert_qa
import pandas as pd
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)


@app.route('/insert', methods=["GET"])
def boostrap_qa():
    excel_qa, db_qa = insert_qa()
    try:
        response = {
            "number_of_QA_in_excel": excel_qa,
            "number_of_QA_inserted_db": db_qa
        }
        return jsonify(response), 200
    except Exception as exc:
        response = {
            "ErrorCode": exc.args[0]
        }
        return jsonify(response)


@app.route('/', methods=["POST"])
def find_answer():
    try:

        if request.method == "POST":

            question_in = request.form.get("question")
            array_of_questions, array_of_answers = get_questions_array()

            last_question, last_confidence = 0, 0

            for question in array_of_questions:
                similarity, formatted_similarity = get_similarity(question, question_in) #როგორ შემიძლია ავიღო სესხი? - შეიძლება?

                if formatted_similarity > last_confidence:
                    last_confidence = formatted_similarity
                    last_question = question
            if last_question:
                result_answer = get_answer_by_question(last_question)
            else:
                result_answer = "მაპატიე, შენს კითხვაზე პასუხი არ მაქვს. შეგიძლია კითხვა სხვანაირა დამისვა?"
            confidence_level = last_confidence

            data = {
                "question_given": request.form["question"],
                "answer": result_answer,
                "question_similar": last_question,
                "confidence_percentage": confidence_level
            }
            return jsonify(data), 200
    except BaseException as exc:
        data = {
            "ErrorCode": exc.args[0]
        }
        return jsonify(data)

