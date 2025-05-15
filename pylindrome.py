import pyinputplus as pyip
import string

def count_words(text):
    words = text.split()
    return len(words)

#Function definition to check if word is a palindrome
def palin_check():
    strng = pyip.inputStr("Enter a word or sentence to check for palindromes!") #User enters suspected palindrome
    strng = strng.lower() #Adjust to lowercase to remove case sensitivity
    strng = strng.strip(string.punctuation) #remove punctuation
    word_count = count_words(strng)

    if word_count == 1:
        word_reversed = strng[::-1] #string slicing reverses word & compares it
        if strng == word_reversed:
            print(f"The word {strng} is a palindrome!")
        else:
            print(f"The word {strng} is not a palindrome.")
    elif word_count > 1: #Sentence Checker
        word_list = strng.split()
        pdromes = []

        #Iterate over every word in the string to check for palindromes
        for word in word_list:
            word_reversed = word[::-1]
            #store palindromes in their own list
            if word == word_reversed:
                pdromes.append(word)

        #Get count of total palindromes and list them out    
        pdrome_count = len(pdromes)
        if pdrome_count == 1:
            print('1 palindrome was detected!')
            print(f'Palindrome: {pdromes[0]}')
        elif pdrome_count > 1:
            print(f'{pdrome_count} palindromes detected!')
            print(f'Palindromes: ')
            for word in pdromes:
                print(word)
        else:
            print('No palindromes were detected...')

#Initial Function Run
palin_check()

#Infinite loop allows for unlimited function re-runs if desired
while True:
    restart = pyip.inputYesNo("Would you like to check another word or sentence? (y/n): ")
    if restart == "yes":
        palin_check()
    else:
        print("Thanks for checking your palindromes with us!")
        break

