from question_model import *
from data import *
from quiz_brain import *
from art import *

print(logo)
print("Welcome to Quiz Game!\n")
question_bank = []

for item in question_data:
    ques = item["text"]
    ans = item["answer"]
    question = Question(ques, ans)
    question_bank.append(question)
quiz = Quiz(question_bank)


while quiz.question_remaining() == True:
    quiz.ask_question()

print("\nThanks for playing quiz game!")
