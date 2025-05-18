# Pylindrome v1.3.0

**Pylindrome** is a lightweight command-line tool that checks for palindromes in either a single word or an entire sentence. Now powered by `typer`, the tool features a modern, user-friendly CLI with improved structure, clarity, and error handling.

---

## What's New in v1.3.0

- Migrated to a command-line interface using `typer`
- Commands split into `word` and `sentence` for precise usage
- Better error handling for empty input
- Punctuation handling for sentence analysis
- Improved output formatting based on palindrome count

---

## Features

- Checks if a **single word** is a palindrome  
- Scans a **sentence** and identifies each word that is a palindrome  
- Displays a **count** and a **list** of detected palindromes  
- Case-insensitive comparison  
- Strips punctuation at the beginning and end of sentences  
- Clean CLI design using `typer`  

---

## How to Use

### Check a Word
```bash
python pylindrome.py word racecar
```
**Output:**
```
The word "racecar" is a palindrome!
```

### Check a Sentence
```bash
python pylindrome.py sentence "Madam Arora teaches malayalam"
```
**Output:**
```
3 palindromes detected!
- madam
- arora
- malayalam
```

---

## Requirements

- Python ≥ 3.6  
- [`typer`](https://pypi.org/project/typer/)

Install the requirement with:
```bash
pip install typer[all]
```

---

## Installation

1. Clone the repository:
```bash
git clone https://github.com/tm4rtin17/Pylindrome
cd Pylindrome
```

2. Run the script using the desired command:
```bash
python pylindrome.py word radar
python pylindrome.py sentence "Wow Anna went to civic center"
```

---

## License

This project is open source and available under the MIT License.
