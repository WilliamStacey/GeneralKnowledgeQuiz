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

instructions()
print("program complete")
