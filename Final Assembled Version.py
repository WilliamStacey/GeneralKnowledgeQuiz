#declare variables

#quiz questions
class Question:
   def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

#question prompt variable
question_prompts = [
  "What is the biggest video game series ever?\n(a) Pokemon\n(b) Mario\n(c) Sonic\nEnter: ",
  "Which movie company has made the most movies?\n(a) Disney\n(b) Universal\n(c) Warner Bros.\nEnter: ",
  "What is the biggest island in the world?\n(a) Greenland\n(b) Madagascar\n(c) Australia\nEnter: ",
  "What is the smallest country?\n(a) Canberra\n(b) The Vatican\n(c) Republic of San Marino\nEnter: ",
  "Who is the richest man in the world?\n(a) Elon Musk\n(b) Bill Gates\n(c) Jeff Bezos\nEnter: ",
 ]

questions = [
   Question(question_prompts[0], "a"),
   Question(question_prompts[1], "b"),
   Question(question_prompts[2], "a"),
   Question(question_prompts[3], "b"),
   Question(question_prompts[4], "c"),
]

#user defined functions

#instructions
def instructions():
    while True:
      rules = input("Would you like to read the instructions? ")

      if rules == "no" or rules == "n" or rules == "N" or rules == "nO" or rules == "No" or rules == "NO" :
        break
          
      elif rules == "yes" or rules == "y" or rules == "Y" or rules == "yeS" or rules == "yEs" or rules == "Yes" or rules == "YEs" or rules == "YES" or rules == "yES" :
        print()
        print("******* Quiz Instructions ********")
        print()
        print("The Instructions are simple for the quiz.")
        print()
        print("Answer the questions that will be provided shortly.")
        print("Once you have decided your answer, don't answer in the name.")
        print("Instead answer in the letter provided that corresponds with the answer you want to make.")
        print("If you do not do that, the answer will automatically be marked as wrong, regardless of if you got it right or not.")
        print("After you have completed the quiz. You will soon get your results")
        print()
        print("That is all. Have fun!")
        print()
        break
        
      else:
        print("Please enter a valid response, such as 'y', 'yes', 'n' or 'no'.")

#ask name
def name():
    global name
    name = ''

    while True:
        name = input("Enter your name: ")
        if name.isalpha():
            break
        print("Please enter characters A-Z only.")

#ask age
def age():
    age = ''

    while True:
        age = input("Enter your age: ")
        if age.isnumeric():
            break
        print("Please enter numbers only.")

#quiz questions
class Question:
   def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

#quiz results
def run_quiz(questions):
   score = 0
   for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
             score += 1
   print("Hey",name)
   print("You got", score, "out of", len(questions))

#print statements

#welcome to quiz
def credits():
  print("*********Welcome to the General Knowledge Quiz*********")
  print("********This Quiz was made by me, William Stacey********")

#calling functions

credits()#credits function
instructions()#instuctions function
name()#name function
age()#age function
run_quiz(questions)#quiz and score function

#Linear Main Routine

#welcome to quiz
def credits():
  print("*********Welcome to the General Knowledge Quiz*********")
  print("********This Quiz was made by me, William Stacey********")

#instructions
def instructions():
    while True:
      rules = input("Would you like to read the instructions? ")

      if rules == "no" or rules == "n" or rules == "N" or rules == "nO" or rules == "No" or rules == "NO" :
        break
          
      elif rules == "yes" or rules == "y" or rules == "Y" or rules == "yeS" or rules == "yEs" or rules == "Yes" or rules == "YEs" or rules == "YES" or rules == "yES" :
        print()
        print("******* Quiz Instructions ********")
        print()
        print("The Instructions are simple for the quiz.")
        print()
        print("Answer the questions that will be provided shortly.")
        print("Once you have decided your answer, don't answer in the name.")
        print("Instead answer in the letter provided that corresponds with the answer you want to make.")
        print("If you do not do that, the answer will automatically be marked as wrong, regardless of if you got it right or not.")
        print("After you have completed the quiz. You will soon get your results")
        print()
        print("That is all. Have fun!")
        print()
        break
        
      else:
        print("Please enter a valid response, such as 'y', 'yes', 'n' or 'no'.")

#ask name
def name():
    global name
    name = ''

    while True:
        name = input("Enter your name: ")
        if name.isalpha():
            break
        print("Please enter characters A-Z only.")

#ask age
def age():
    age = ''

    while True:
        age = input("Enter your age: ")
        if age.isnumeric():
            break
        print("Please enter numbers only.")


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

#quiz results
def run_quiz(questions):
   score = 0
   for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
             score += 1
   print("Hey",name)
   print("You got", score, "out of", len(questions))
