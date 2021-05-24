#quiz questions
class Question:
   def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

question_prompts = [
  "What is the biggest video game series ever?\n(a) Pokemon\n(b) Mario\n(c) Sonic\nEnter: ",
  "Which movie company has made the most movies?\n(a) Disney\n(b) Universal\n(c) Warner Bros.\nEnter: ",
  "What is the biggest island in the world?\n(a) Greenland\n(b) Madagascar\n(c) Australia\nEnter: ",
  "What is the smallest country?\n(a) Canberra\n(b) The Vatican\n(c) Republic of San Marino\nEnter: ",
  "Who is the richest man in the world?\n(a) Elon Musk\n(b) Bill Gates\n(c) Jeff Bezos\nEnter: ",
 ]

questions = [
   Question(question_prompts[0], "a" or "pokemon" or "Pokemon"),
   Question(question_prompts[1], "b"),
   Question(question_prompts[2], "a"),
   Question(question_prompts[3], "b"),
   Question(question_prompts[4], "c"),
]
