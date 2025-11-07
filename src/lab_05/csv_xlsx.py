import pandas as pd
from pathlib import Path
from openpyxl import Workbook
import csv
import sys

sys.path.append('/Applications/Python_3.13/proga/py_labs/data/lab_04/')
from io_txt_csv import *

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Конвертирует CSV в XLSX.
    Использовать openpyxl ИЛИ xlsxwriter.
    Первая строка CSV — заголовок.
    Лист называется "Sheet1".
    Колонки — автоширина по длине текста (не менее 8 символов).
    """
    

    read_text(csv_path)


    wb = Workbook()
    ws = wb.active

    with open(csv_path, 'r', newline='', encoding='utf-8') as csvfile:

        reader = csv.reader(csvfile)
        

        for row in reader:
            ws.append(row)

    for column_cells in ws.columns:
  
        column_letter = column_cells[0].column_letter
        ws.column_dimensions[column_letter].auto_size = True
 
    wb.save(xlsx_path)


csv_path = Path('/Applications/Python_3.13/proga/py_labs/data/samples/people.csv')
xlsx_path = Path('/Applications/Python_3.13/proga/py_labs/data/out/people.xlsx')

csv_to_xlsx(csv_path,xlsx_path)