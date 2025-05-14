# Pylindrome v1.1

This Python script allows users to check whether a **word** or **sentence** contains **palindromes**. With enhanced interactivity and multi-word support, you can now analyze complete sentences and get a list of detected palindromes. 

---

## What's New in v1.1

Sentence support – analyze multiple words at once
Case-insensitive comparisons
Count and display of all detected palindromes
Cleaner logic and user-friendly feedback

---

## Features

* Verifies if a **single word** is a palindrome
* Detects **multiple palindromes** in a **sentence**
* Displays total count and the list of detected palindromes
* Interactive input with validation via the `pyinputplus` library
* Option to run multiple checks in a single session

---

## How It Works

1. **Input**
   The user enters either a word or a full sentence.

2. **Processing**

   * If one word is entered, the script checks if it reads the same forwards and backwards.
   * If a sentence is entered, the script evaluates each word independently.

3. **Output**

   * A message indicates whether the word is a palindrome.
   * For sentences, the number of palindromes is shown along with the list.

4. **Repeat Option**
   After each run, the user can choose to check another word or sentence.

---

## Requirements

* Python 3.13.1
* `pyinputplus` library

---

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/tm4rtin17/Pylindrome
   ```

2. Install the required library:

   ```bash
   pip install pyinputplus
   ```

---

## Usage

1. Run the script:

   ```bash
   python pylindrome.py
   ```

2. Follow the on-screen prompts 🧾

3. Type `n` when asked if you'd like to check another input to exit 🚪

---

## Example Interactions

```plaintext
Enter a word or sentence to check for palindromes!: radar
The word radar is a palindrome!
Would you like to check another word or sentence? (y/n): y
Enter a word or sentence to check for palindromes!: My mom and dad went to the mall
2 palindromes detected!
Palindromes:
mom
dad
Would you like to check another word or sentence? (y/n): n
Thanks for checking your palindromes with us!
```

---

## Contributing

Fork this repo and submit a pull request!
Suggestions for punctuation handling, UI improvements, or full sentence palindrome logic are welcome!

---

## License

This project is licensed under the MIT License 📜

---
