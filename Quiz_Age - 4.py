#ask age
age = ''

while True:
    age = input("Enter your age: ")
    if age.isnumeric():
        break
    print("Please enter whole numbers only.")

print("You are",age)
