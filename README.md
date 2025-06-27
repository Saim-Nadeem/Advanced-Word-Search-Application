📚 Advanced Word Search Application (GUI + KMP + Brute Force)

[![Python](https://img.shields.io/badge/Built%20with-Python-blue.svg)](https://www.python.org/)
[![Tkinter](https://img.shields.io/badge/GUI-Tkinter-orange.svg)](https://wiki.python.org/moin/TkInter)
[![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A modern GUI-based Python application to search for specific terms inside multiple `.txt` files using **Brute Force** or **KMP (Knuth-Morris-Pratt)** string matching algorithms. Features include whole word matching, case sensitivity, result highlighting, and time analysis.

---

## 🎯 Key Features

- 🔎 Search across multiple selected `.txt` files
- ✅ Select from:
  - Brute Force Search
  - KMP Search (Efficient for longer texts)
- 🎛️ Options:
  - Whole Word Match toggle
  - Case Sensitivity toggle
- ⏱️ Shows time taken for search
- 💡 Highlights search results in context
- 🖥️ GUI built with `tkinter` and `ttk` themes

---

## 📦 Requirements

- Python 3.7 or higher
- Tkinter (comes preinstalled with most Python distributions)

To install the only required module (`tk`), run:

```bash
pip install -r requirements.txt
```

⚠️ On Linux systems, if tkinter isn't working:

```bash
sudo apt install python3-tk
```

---

## 🚀 How to Run

1️⃣ Clone or download this repository  
2️⃣ Open your terminal or command prompt  
3️⃣ Navigate to the project folder  
4️⃣ Install dependencies:

```bash
pip install -r requirements.txt
```

5️⃣ Run the application:

```bash
python word_search_gui.py
```

✅ A GUI window will launch. You’re ready to search!

---

## 🧠 Algorithms Used

### Brute Force
- Compares each character in the text against the search pattern
- Simple and effective for small-scale searches

### Knuth-Morris-Pratt (KMP)
- Efficient in handling large strings by skipping redundant comparisons
- Uses a **Longest Prefix Suffix (LPS)** array

---

## 🧭 User Instructions

1. Launch the app by running `word_search_gui.py`
2. Click **“Select Files”** to choose `.txt` files
3. Type a **search term**
4. Select your options:
   - ✅ Whole Word Match
   - ✅ Case Sensitive
   - ✅ Algorithm: Brute Force or KMP
5. Click **“Search”**
6. Results will be displayed below with matches and context

---

## 📊 Sample Output (Displayed in App)

```
Searching for 'example' in 2 files
Options: Case Sensitive: False, Whole Word: True, Algorithm: KMP

File: sample1.txt
Found 3 occurrences
[Pos 42]: ...this is an Example line with the word example...
[Pos 108]: ...some more example text with example usage...

File: sample2.txt
Found 1 occurrences
[Pos 33]: ...this is the only example here...

Search completed in 0.0024 seconds.
Total occurrences found: 4
```

---

## 🖼️ GUI Overview

- Dark theme using `ttk` clam style
- Search box with custom font
- Search options (checkboxes + radio buttons)
- Scrollable result area with color highlights
- Status bar to show real-time progress

---

## ⚠️ Error Handling

- If search term is empty → Shows a warning
- If no file is selected → Prompts user to select files
- If file encoding fails → Displays detailed error message

---

## 📁 Project Structure

```
├── word_search_gui.py         # Main application script
├── requirements.txt           # Dependency list
├── README.md                  # Project documentation
└── LICENSE                    # MIT License file
```

---

## 🔐 License

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for full terms.

---

## 🙌 Acknowledgments

- Developed as a text processing and algorithmic GUI project using Python  
- Inspired by real-world search use-cases and CS course learning  
- References:
  - https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/
  - https://www.youtube.com/watch?v=yMJLpdKV0BQ
  - https://www.geeksforgeeks.org/python-gui-tkinter/
  - https://www.geeksforgeeks.org/python-os-path-basename-method/

---

## 👤 Author

**Saim Nadeem**  
🔗 GitHub: [Saim-Nadeem](https://github.com/Saim-Nadeem)

---
