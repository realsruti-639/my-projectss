# 📊 Personal Finance Tracker

A lightweight, robust, and zero-dependency terminal application built in **Python** for tracking personal finances and expense logging. This application utilizes **Object-Oriented Programming (OOP)** principles and directly aggregates analytical financial data natively through filesystem streaming.

---

## 💡 Key Engineering Features

- **Local Storage Management:** Streams entries directly to a persistent, locally structured `CSV` database, completely optimizing application storage parameters.
- **Dynamic Analytical Summary:** Automatically computes aggregated totals, transactional category weights, and distribution percentages.
- **Visual Text Dashboards:** Generates custom ASCII graphical progress bars built directly into the UI text lanes for visual trend analysis without heavy dependency requirements.
- **Error-Resilient Interface:** Formatted validation routines protect input parameters against unexpected value type breakdowns.

---

## 🛠️ Architecture & Tech Stack

- **Core Engine:** Python 3.x
- **Data Layer:** `csv` & `os` standard libraries (Buffered persistent filesystem storage)
- **Version Control:** Git & GitHub

---

## 🚀 Execution & Setup Instructions

To run this application locally on your machine, navigate to your workspace folder and execute:

```bash
python tracker.py
```

### Application Menu Layout:
1. **Add New Expense:** Interactive prompts capture transaction parameters (Date, Category, Value, Info).
2. **View Expense Log:** Displays tabular readouts of all historically committed entries.
3. **View Finance Summary Report:** Renders analytical distribution breakdowns and graphical progress meters.
4. **Exit:** Safely closes file operations and logs out.
