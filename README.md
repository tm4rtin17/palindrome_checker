# 🌀 Pylindrome v1.2.0

**Pylindrome** is a Python script that checks whether a **word** or **sentence** contains **palindromes**. With clean separation between word and sentence analysis, this version improves clarity, flexibility, and reusability.

---

## 🆕 What's New in v1.2.0

- ✅ Separated logic into dedicated functions: `word_check()` and `sentence_check()`
- 🎯 Cleaner input prompts for word vs sentence detection
- 🧼 Streamlined output formatting with clearer messages
- 🪝 Main menu for choosing between word or sentence check
- 🔁 Infinite loop restructured for better readability and flow

---

## ✨ Features

- 🧪 Checks if a **single word** is a palindrome  
- 📚 Detects and lists all **palindromes in a sentence**
- 📊 Displays **total count** and a formatted **list**
- 🧠 Case-insensitive comparisons
- 🧹 Filters out punctuation at the edges
- 🔁 Menu-based reruns for continuous input
- 🔐 Input safety via `pyinputplus` validation

---

## ⚙️ How It Works

1. **Startup**  
   You're prompted to choose between checking a single word or a sentence.

2. **Input**
   - Word: A single term is tested.
   - Sentence: Each word in the sentence is evaluated.

3. **Processing**
   - Reverses each word to compare it.
   - Ignores case differences.
   - Filters out surrounding punctuation from sentences.

4. **Output**
   - Displays whether the input is a palindrome (for words).
   - Shows the count and list of palindromes (for sentences).

5. **Repeat**
   - You're prompted after each check if you'd like to try again.

---

## 🧰 Requirements

- Python ≥ 3.6 (tested on 3.13.1)
- [`pyinputplus`](https://pypi.org/project/PyInputPlus/)

---

## 🚀 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/tm4rtin17/Pylindrome
   cd Pylindrome
