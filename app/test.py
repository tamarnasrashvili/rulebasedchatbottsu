from similarity import get_similarity
from question_orm import get_questions_array, get_answer_by_question

q_in = "გადარიცხვას ააქვს ლიმიტი?"

array_of_questions, array_of_answers = get_questions_array()

last_question, last_confidence = 0, 0

for question in array_of_questions:
    similarity, formatted_similarity = get_similarity(question, q_in)

    print(similarity, formatted_similarity)
