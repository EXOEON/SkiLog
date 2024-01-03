import csv
from flask import Flask, render_template, request, jsonify

from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func

csv_file = 'BV-Trails.csv'

fs = []
bs = []
lm = []
vs = []

with open(csv_file, 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        if row[2] == 'fs':
            fs.append(row)
        elif row[2] == 'bs':
            bs.append(row)
        elif row[2] == 'lm':
            lm.append(row)
        elif row[2] == 'vs':
            vs.append(row)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', fs=fs, bs=bs, lm=lm, vs=vs)

checkbox_states = {}

@app.route('/update_checkbox', methods=['POST'])
def update_checkbox():
    data = request.get_json()
    checkbox_id = data.get('id')
    checked = data.get('checked')
    checkbox_states[checkbox_id] = checked
    return jsonify({'message': 'Checkbox state updated successfully'})

@app.route('/get_checkbox_states', methods=['GET'])
def get_checkbox_states():
    return jsonify(checkbox_states)

if __name__ == '__main__':
    app.run(debug=True)
