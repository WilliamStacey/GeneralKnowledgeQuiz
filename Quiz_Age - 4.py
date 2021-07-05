#ask age
def age():
    age = ''

    while True:
          age = input("Enter your age: ")
          if age.isnumeric():
              break
          print("Please enter numbers only.")

print("You are",age)
age()
