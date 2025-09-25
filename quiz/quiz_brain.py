class QuizBrain():
    def __init__(self, q_list):
        self.question_list = q_list
        self.question_no = 0
        self.correct_answers = 0

    def next_question(self):
        question=self.question_list[self.question_no]
        self.question_no += 1
        print(f'Q{self.question_no}. {question.text}')
        answer_user=input('True/False: ')
        self.check_answer(answer_user, question.awnser) 
        
    def check_answer(self, answer_user, correct_answer):
        if answer_user.lower() == correct_answer.lower() :
            print('Correct answer!')
            answer_status = True
        elif answer_user.lower != correct_answer.lower :
            print(f'Ahhh! Sorry thats the wrong awnser \nThe correct answer is {correct_answer}')
            answer_status = False
        self.score_counter(answer_status )
        
    def score_counter(self, status):
        if status == True:
            self.correct_answers += 1
        else:
            pass
        print(f'{self.correct_answers}/{self.question_no}')        