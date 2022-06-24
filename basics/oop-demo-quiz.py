
# Ne kadar az if-else yazıyorsan o kadar kaliteli kod yazıyorsun demektir.

# Question

class Question:
    def __init__(self, text, choices, answer): #initializer
        self.text = text                       # Dışarıdan alınan soru
        self.choices = choices                 # Dışarıdan alınan dizi
        self.answer = answer                   # Dışarıdan alınan cevap
        
    def checkAnswer(self, answer):
        return self.answer == answer

# Quiz

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]

    def displayQuestion(self):
        question = self.getQuestion()
        print(f'Soru {self.questionIndex + 1}: {question.text}')

        for q in question.choices:
            print('-' + q)

        answer = input('cevap: ')
        self.guess(answer)
    
    def guess(self, answer):
        question = self.getQuestion()

        if question.checkAnswer(answer):
            self.score += 1
        self.questionIndex += 1
        self.loadQuestion()

    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()

    def showScore(self):
        print('Score: ', self.score)

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1

        if questionNumber > totalQuestion:
            print('Quiz bitti')
        else:
            print(f'Question {questionNumber} of {totalQuestion}'.center(100, '*'))

q1 = Question('en iyi programlama dili hangisidir?', ['C#','Python','Java','Javascript'], 'Python')
q2 = Question('en popüler programlama dili hangisidir?', ['Python','Java','C#','Javascript'], 'Python')
q3 = Question('en çok kazandıran programlama dili hangisidir?', ['C#','Java','Python','Javascript'], 'Python')
q4 = Question('en çok sevilen programlama dili hangisidir?', ['C#','Java','Python','Javascript'], 'Python')
q5 = Question('en kolay programlama dili hangisidir?', ['C#','Java','Python','Javascript'], 'Python')

questions = [q1, q2, q3, q4, q5]

quiz = Quiz(questions)
quiz.loadQuestion()