# 📊 XLSX to CSV Converter (Multi-Sheet Support)

This Python script automatically converts all `.xlsx` Excel files from a specified input folder into `.csv` files — including **every sheet** from each Excel file. Each sheet is saved as an individual CSV in the output folder.

---

## ✅ Features

- Converts all `.xlsx` files in the input directory
- Saves each sheet as a separate `.csv` file
- Automatically names output files using format: `final_<filename>_<sheetname>.csv`
- Uses `pandas` and `openpyxl` for reliable Excel parsing

---

## 📦 Requirements

Make sure you have Python 3.7+ installed. Then install required libraries:

```bash
pip install pandas openpyxl
