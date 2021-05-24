#instructions
while True:
  rules = input("Would you like to read the instructions? ")

  if rules == "no" or rules == "n" :
    break
      
  elif rules == "yes" or rules == "y" :
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

print("program complete")
