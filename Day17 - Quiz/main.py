from data import question_data
from question_model import Question
from quiz_brain import Brain

question_bank = []

for i in question_data:
    
    text = i["text"]
    answer = i["answer"]
    question_bank.append(Question(text, answer))

brain = Brain(question_bank)

while brain.question_remain():
    if brain.next_question():
        brain.check_answer()

print("You have finished the Quiz !!!")
print(f"Your Final Score was {brain.score}/{brain.question_number}")