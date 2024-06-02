from question_model import Question
from data import question_data
from quize_brain import QuizBrain
from ui import QuizInterface

"""crating a list that contains random question from Trivio database"""
question_bank = []
for i in question_data:
    question = i["question"]
    answer = i["correct_answer"]
    new_question = Question(question, answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
my_quiz = QuizInterface(quiz)
"""While loop will run until reach 10th question"""
while quiz.still_have_question():
    quiz.next_question()


