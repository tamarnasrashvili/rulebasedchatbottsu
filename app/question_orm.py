from app import Question, db


def get_questions_array():
    questions = []
    answers = []
    for question in Question.query.all():
        questions.append(question.question)
        answers.append(question.answer)
    print(questions)
    return questions, answers


def get_answer_by_question(question):
    answer = db.session.query(Question.answer).filter_by(question=question).first()[0]
    print(answer)
    return answer

