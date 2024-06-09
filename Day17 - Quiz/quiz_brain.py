class Brain:

    def __init__(self, list):
        self.question_number = 0
        self.question_list = list
        self.score = 0

    def next_question(self):

        current_question = self.question_list[self.question_number]
        self.question_number += 1

        user = input(f" Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user, current_question.answer)

    def question_remain(self):

        if self.question_number < len(self.question_list):
            return True
        else:
            return False
        
    def check_answer(self, user, correct_ans):

        if user.lower() == correct_ans.lower():
            print("Yayyy!! You got it right")
            self.score += 1
        
        else:
            print("Thats Wrong...")
        
        print(f"Score: {self.score}/{self.question_number}")
        print("")

        
            
