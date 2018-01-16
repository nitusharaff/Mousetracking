class quiz:


    def __init__(self):
        self.ques_file="Questions/all_ques.txt"
        self.question=[]
        self.quesid=[]
        self.numQues=0

    def getQuestionId(self,quizid):
        file = "Quiz/"+ quizid + ".txt"
        with open(file) as inp:
          for x in inp.readlines():
            self.quesid.append(x.strip().split(",")[1])
        return self.quesid


    def getQuestions(self,quizid):
        self.getQuestionId(quizid=quizid)
        for id in self.quesid:
            with open(self.ques_file) as inp:
                for line in inp.readlines():
                    word=line.strip().split(",")
                    if(id== word[0]):
                        self.question.append(word[3])
        self.numQues= len(self.question)
        return self.question



