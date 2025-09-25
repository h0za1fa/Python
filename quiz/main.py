from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_index=[]

for questions in question_data:
    question=Question(questions['text'],questions['answer'] )
    question_index.append(question)

quiz_brain = QuizBrain(question_index)

for n in range (len(question_index)):
    quiz_brain.next_question()
    print('\n')
    
print('You finished the quiz!')
print(f'You scored {quiz_brain.correct_answers}/{quiz_brain.question_no}')