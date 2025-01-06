import pyinputplus as pyip

#Function definition to check if word is a palindrome
def palin_check():
    word = pyip.inputStr("Enter a word to see if it is a palindrome!") #User enters suspected palindrome
    word_reversed = word[::-1] #string slicing reverses word

    #Word match logic; Prints Result
    if word == word_reversed:
        print(f"The word {word} is a palindrome!")
    else:
        print(f"The word {word} is not a palindrome.")

#Initial Function Run
palin_check()

#Infinite loop allows for unlimited function re-runs if desired
while True:
    restart = pyip.inputYesNo("Would you like to check another word? (y/n): ")
    if restart == "yes":
        palin_check()
    else:
        print("Thanks for checking your palindromes with us! Come back soon!")
        break

