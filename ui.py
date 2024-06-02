from tkinter import *
from quize_brain import QuizBrain
from tkinter import messagebox

THEME_COLOR = "#FFEFEF"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain
        """creating a user interface window"""
        self.window = Tk()
        self.window.title("Quiz Game")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        """adding elements in window"""
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.ques_text = self.canvas.create_text(
            150, 130,
            width=280,
            text="xx",
            fill="black",
            font=("Arial", 20, "italic"))
        self.score_labe = Label(text="Score:0", bg=THEME_COLOR, fg="black",font=("Arial",9,"bold"))
        self.score_labe.grid(column=1, row=0)
        right_img = PhotoImage(file="right.png")
        self.right_button = Button(image=right_img, highlightthickness=0, command=self.true_check)
        self.right_button.grid(column=0, row=2)
        wrong_img = PhotoImage(file="wrong.png")
        self.wrong_button = Button(image=wrong_img, highlightthickness=0, command=self.false_check)
        self.wrong_button.grid(column=1, row=2)
        self.get_next_question()
        self.window.mainloop()

    """Retrieving question from quiz_brain question_list by calling it"""
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz_brain.still_have_question():
            self.score_labe.config(text=f"Score:{self.quiz_brain.score}")
            ques_text = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.ques_text, text=ques_text)
        else:
            self.canvas.itemconfig(self.ques_text,text="End of Quize")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")
            self.window.after(300)
            messagebox.showinfo(title="Quiz Result",
                                message=f"Congratulation!Your Total Score is {self.quiz_brain.score}/10 ")

    """checking for Ture"""
    def true_check(self):
        self.user_answer_check(self.quiz_brain.check_answer("True"))

    """checking for false"""
    def false_check(self):
        self.user_answer_check(self.quiz_brain.check_answer("False"))

    def user_answer_check(self, is_right):
        self.canvas.config(bg="green") if is_right == True else self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
