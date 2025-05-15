# 🌀 Pylindrome v1.1.01

**Pylindrome** is a Python script that checks whether a **word** or **sentence** contains **palindromes**. With enhanced sentence analysis, cleaner logic, and replay support, it's a fun tool to explore word symmetry in real time.

---

## 🆕 What's New in v1.1.01

* 🩹 Version bump for internal improvements
* 🔤 Fine-tuned punctuation handling
* 🧼 Code formatting and readability enhancements
* 📄 Minor docstring/print message cleanup

---

## ✨ Features

* 🧪 Checks if a **single word** is a palindrome
* 🔍 Analyzes **each word** in a **sentence** for palindromes
* 📊 Displays a **count** and **list** of all detected palindromes
* 🔄 Offers continuous input until the user opts out
* 🔐 Uses `pyinputplus` for validated, user-safe input

---

## ⚙️ How It Works

1. **Input**
   Enter a single word or an entire sentence.

2. **Processing**

   * If one word is entered, it's checked for being a palindrome.
   * If multiple words are entered, **each word** is checked individually.
   * The check is case-insensitive and ignores leading/trailing punctuation.

3. **Output**

   * Clear feedback on whether the word is a palindrome.
   * For sentences: a **count** and **list** of palindromes found.

4. **Repeat**

   * You're prompted after each run to check another word/sentence.

---

## 🧰 Requirements

* Python ≥ 3.6 (tested on 3.13.1)
* [`pyinputplus`](https://pypi.org/project/PyInputPlus/)

---

## 🚀 Installation

1. Clone the repo:

   ```bash
   git clone https://github.com/tm4rtin17/Pylindrome
   cd Pylindrome
   ```
