class QuestionModel:
    category: str
    type: str
    difficulty: str
    question: str
    correct_answer: str

    def __init__(self, category, type, difficulty, question, correct_answer):
        self.category = category
        self.type = type
        self.difficulty = difficulty
        self.question = question
        self.correct_answer = correct_answer
