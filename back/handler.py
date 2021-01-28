from flask import Flask, render_template, jsonify, request
from flask_cors import CORS



# app = Flask(__name__, static_folder = "./../front/dist/static", template_folder="./../front/dist")
app = Flask(__name__)
CORS(app)
@app.route('/upload', methods=['POST'])
def handler():
  file = request.form.get('file')
  response={'file': file}
  return jsonify(response)

if __name__ == '__main__':
    app.run()

