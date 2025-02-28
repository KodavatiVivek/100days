from questionmodel import Question   # This line is added to import the Question class from question_model.py
from data import question_data        # This line is added to import the question_data list from data.py
from Brain import QuizBrain     # This line is added to import the QuizBrain class from Quiz_brain.py
from newdata import question_data     # This line is added to import the question_data list from newdata.py

question_bank = []     # This line is added to create an empty list
for question in question_data:
    text = question["question"]
    answer = question["correct_answer"]
    question_bank.append(Question(text, answer))# This line is added to append the Question object to the question_bank list

quiz=QuizBrain(question_bank)   # This line is added to create a QuizBrain object and pass the question_bank list to it

print("Welcome to Quizzler!\n")
print("Answer the following questions with True or False.\n")
print("Good Luck!\n")
# This line is added to print the welcome message
print("Each correct answer will give you 1 point.\n")
while quiz.still_has_questions():
    quiz.next_question()   # This line is added to call the next_question method of the quiz object

print("You have completed the quiz.")
print(f"Your final score is {quiz.score} out of {quiz.question_number}")