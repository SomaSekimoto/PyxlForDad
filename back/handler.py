from flask import Flask, request, send_file
from flask_cors import CORS
import auto
import base64
import datetime
import os
import shutil



app = Flask(__name__)
CORS(app)
@app.route('/upload', methods=['POST'])
def handler():
  binary_data = request.form.get('file')
  decoded = base64.b64decode(binary_data.split(',')[1])

  now = datetime.datetime.now()
  datetime_str = now.strftime(f"%Y%m%d%H%M%S")
  dir_name = './files'
  shutil.rmtree(dir_name)
  os.mkdir(dir_name)
  file_name = dir_name + "/Book" + datetime_str + ".xlsx"
  print(file_name)
  with open(file_name, "wb") as f:
        f.write(decoded)

  file = auto.create_shift(file_name)

  XLSX_MIMETYPE = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
  return send_file(file_name, mimetype = XLSX_MIMETYPE)

if __name__ == '__main__':
    app.run()

