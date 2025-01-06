# Palindrome Checker

This Python script allows users to check whether a given word is a palindrome. It provides an intuitive and interactive experience with user-friendly prompts.

## Features
- Verifies if a word is a palindrome.
- Provides an option to check multiple words in a single session.
- Interactive input validation using the `pyinputplus` library.

## How It Works
1. **Palindrome Check:**
   - The user enters a word.
   - The script checks if the word is the same when read forwards and backwards.
   - It displays whether the word is a palindrome.

2. **Restart Option:**
   - After each check, the user is prompted to either check another word or exit the program.
   - The program runs continuously until the user chooses to exit.

## Requirements
- Python 3.13.1
- `pyinputplus` library

## Installation
1. Clone this repository:
   ```bash
   git clone <repository_url>
   ```
2. Install the required library using pip:
   ```bash
   pip install pyinputplus
   ```

## Usage
1. Run the script:
   ```bash
   python palindrome_checker.py
   ```
2. Follow the on-screen prompts to check if a word is a palindrome.
3. To exit, respond with "n" when asked if you'd like to check another word.

## Example Interaction
```plaintext
Enter a word to see if it is a palindrome!: radar
The word radar is a palindrome!
Would you like to check another word? (y/n): y
Enter a word to see if it is a palindrome!: hello
The word hello is not a palindrome.
Would you like to check another word? (y/n): n
Thanks for checking your palindromes with us! Come back soon!
```

## Contributing
Feel free to fork this repository and submit pull requests if you'd like to enhance the script or add new features.

## License
This project is licensed under the MIT License.

---

Happy palindrome checking!
