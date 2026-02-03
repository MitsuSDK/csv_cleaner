# CSV Cleaner 🧹

A simple and robust **Python CLI tool** to clean CSV files by:
- normalizing fields (trimming whitespace),
- removing empty rows,
- optionally removing duplicate rows.

This project was built to practice **data preprocessing**, **modular Python design**, and **command-line interfaces**, which are said to be core skills for data and AI-oriented workflows.

---

## ✨ Features

- Clean CSV fields by removing leading and trailing whitespace
- Remove empty rows
- Optional row deduplication
- Simple and clear command-line interface
- Uses only the Python standard library

---

## 📂 Project Structure

```text
csv_cleaner/
│
├── csv_cleaner.py      # Main script (logic + CLI)
├── README.md
└── samples/
    ├── messy.csv       # Example input file
    └── cleaned.csv     # Example output file (appears once the program is executed)