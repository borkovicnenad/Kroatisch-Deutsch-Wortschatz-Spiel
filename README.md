# Wortschatz Trainer

A command-line vocabulary trainer for practicing **German → Croatian** word translations (with articles) using a custom CSV dictionary.

---

## Overview

This program:

* Loads a German vocabulary list from a semicolon-separated CSV file.
* Prompts you with the Croatian meaning.
* You enter the German translation (including the article if applicable).
* Tracks your performance in real time.
* Saves the session results to a statistics CSV file for later review.

---

## Project Structure

```
.
├── wortschatz.py               # Main Python script
├── Wortschatz/
│   └── Deutsch-2.csv           # Dictionary CSV (semicolon-separated, UTF-8)
├── Statistiken.csv              # Session results log (auto-generated/appended)
```

---

## CSV Format

Your dictionary file must be **UTF-8 encoded** and use **`;`** as the delimiter.
The program expects **at least 6 columns** in this order:

| Column Index | Field    | Description                                          |
| ------------ | -------- | ---------------------------------------------------- |
| 0            | type     | Word category (e.g., noun, verb)                     |
| 1            | article  | `der`, `die`, `das`, or `/` if no article            |
| 2            | word     | German word (without article)                        |
| 3            | sufixes  | Extra info (plural form, past tense, suffixes, etc.) |
| 4            | croatian | Croatian translation (used for prompts)              |
| 5            | example  | Example sentence (not shown in quiz by default)      |

**Example:**

```
Substantiv;der;Tisch;Plural: Tische;stol;Der Tisch ist rund.
```

If a row has fewer than 6 columns, it will be skipped.

---

## Statistics File

After each session, results are appended to `Statistiken.csv` in the following format:

```
<datetime>;<time_played>;<dictionary_name>;<points>;<total_attempts>;<accuracy_percent>
```

Example:

```
2025-08-12 19:24:53.123456;00:10:32;Deutsch-2.csv;40;50;80.0
```

---

## Requirements

* Python 3.8+
* [`termcolor`](https://pypi.org/project/termcolor/) library for colored output.

---

## Installation

### **Option 1 — Virtual environment (recommended)**

```bash
python3 -m venv venv
source venv/bin/activate
pip install termcolor
```

### **Option 2 — Debian/Ubuntu system packages**

```bash
sudo apt update
sudo apt install python3-termcolor
```

---

## Running the Program

From the project root:

```bash
python3 wortschatz.py
```

You will see:

```
Hallo, Sie verwenden derzeit das Deutsch-2.csv Wörterbuch. Um das Spiel zu beenden, geben Sie „exit“ ein!
```

Then the prompt will display a Croatian word:

```
stol:
```

Type the correct German translation with the article (if present):

```
der Tisch
```

---

## Gameplay Rules

* **Correct answer** → Shows suffix info, prints **KORREKT!** in green, updates score.
* **Wrong answer** → Shows correct German word, suffix info, prints **FALSCH!** in red.
* **Exit** → Type `exit` to finish and save results.

---

## Customization

* To change the dictionary file:

  ```python
  dictionary_file_path = './Wortschatz/Deutsch-2.csv'
  ```
* To show example sentences, add:

  ```python
  print(current_word.example)
  ```

  after displaying the suffix.


---
## CSV File Preparation (Separator & Cleanup)

### 1. Remove all `;` characters (in-place)

The following command removes all occurrences of the `;` character from **Deutsch-B1.csv** and overwrites the same file:

```bash
sed -i '' 's/;//g' Deutsch-B1.csv