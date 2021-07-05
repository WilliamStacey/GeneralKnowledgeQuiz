#ask name
def name():
    global name
    name = ''

    while True:
        name = input("Enter your name: ")
        if name.isalpha():
            break
        print("Please enter characters A-Z only.")

name()
print("program complete")
