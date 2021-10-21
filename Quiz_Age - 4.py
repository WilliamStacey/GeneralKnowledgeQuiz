#ask age
def age():
    age = ''

    while True:
      try:
        age = int(input("Enter your age: "))
        if age < 10:
            print("You are too young to take this quiz.")
            raise SystemExit
        elif age > 18:
            print("You are too old to take this quiz.")
            raise SystemExit
        break
      except ValueError:
        print("Please enter numbers only.")

age()
print("program complete")
