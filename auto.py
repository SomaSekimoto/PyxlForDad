from openpyxl import load_workbook
import random


wb = load_workbook(filename = 'Book1.xlsx')
sheet_ranges = wb['202102 (2) Copy']
sheet_ranges['W12'].value = 6
ws2_copy = wb.copy_worksheet(wb["202102 (2)"])
sr = sheet_ranges['F5':'I8']
tables = []
for col in sheet_ranges.iter_cols(min_row=5, max_row=16, min_col=6, max_col=33):
  col_vals = []
  for cell in col:
    print(cell.value)
    col_vals.append(cell.value)
  tables.append(col_vals)
print(tables)
for col in tables:
  num = [1,2,3,4,5,6,7,8,9,10]
  random.shuffle(num)
  for index, cell in enumerate(col):
    if cell is None:
      print(index)
      print(num)
      col[index] = num[0]
      num.pop(0)
print(tables)
wb.save('Book1.xlsx')

