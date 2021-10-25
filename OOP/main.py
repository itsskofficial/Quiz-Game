from question_model import *
from data import *
from quiz_brain import *
from art import *

print(logo)
print("\nWelcome to Quiz Game!")
question_bank = []
i = 0
for key, value in question_data[i].items():
    question = Question(key, value)
    question_bank.append(question)
    i += 1
quiz = Quiz(question_bank)


while quiz.question_remaining() == True:
    quiz.ask_question()
