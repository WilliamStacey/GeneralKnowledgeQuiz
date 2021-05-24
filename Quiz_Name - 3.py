#ask name

while True:
    name = input("Enter your name: ")
    if name.isalpha():
        break
    print("Please enter characters A-Z only.")

