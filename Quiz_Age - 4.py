#ask age
def age():
    age = ''

    while True:
          age = input("Enter your age: ")
          if age.isnumeric():
              break
          print("Please enter numbers only.")

age()
print("program complete")
