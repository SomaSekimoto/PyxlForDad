from openpyxl import load_workbook
import random
import datetime

wb = load_workbook(filename = 'Book1.xlsx')
sheet_names = wb.sheetnames
sheet = wb[sheet_names[0]]
copy_sheet = wb.copy_worksheet(sheet)
now = datetime.datetime.now()
copy_sheet.title = 'NewShift' + now.strftime(f'%Y%m%d%H%M%S')
tables = []
cell_ranges = copy_sheet.iter_cols(min_row=5, max_row=16, min_col=6, max_col=33)
for index, col in enumerate(cell_ranges):
  num = [1,2,3,4,5,6,7,8,9,10]
  random.shuffle(num)
  if index == 1:
    array = []
    print(len(array))
    while len(array) < 10:
      # print(tables[index - 1])
      for i, cell in enumerate(tables[index - 1]):
        if cell == num[i]:
          print('a')
          random.shuffle(num)
          array = []
          continue
        else:
          print('b')
          array.append(0)
  elif index > 1:
    while len(array) < 10:
      for i, cell in enumerate(tables[index - 1]):
        if cell == num[i]:
          print('c')
          random.shuffle(num)
          array = []
          continue
        else:
          print('d')
          array.append(0)
      for i, cell in enumerate(tables[index - 2]):
        if cell == num[i]:
          print('e')
          random.shuffle(num)
          array = []
          continue
        else:
          print('f')
          array.append(0)

  col_vals = []
  for i, cell in enumerate(col):
    print(num)
    if len(num) > 0 and cell.value is None:
      print(cell.value)
      cell.value = num[0]
      col_vals.append(cell.value)
      num.pop(0)


  tables.append(col_vals)
print(tables)
wb.save('Book1.xlsx')

