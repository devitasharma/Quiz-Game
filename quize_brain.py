import html

class QuizBrain:
    def __init__(self, question_list):
        self.question = None
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    """ track number of question left in list."""
    def still_have_question(self):
        return self.question_number < len(self.question_list)
    """Retrieving question & answer from question_list one by one & store it in defined variables."""
    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        self.correct_answer = self.current_question.answer
        return f"Q.{self.question_number}:{q_text}"
    """compare user answer with original answer """
    def check_answer(self,user_input):
        if user_input.lower() == self.correct_answer.lower():
            self.score += 1
            return True

        else:
            return False
