import csv
from flask import Flask, render_template, request, redirect, url_for, session

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

if __name__ == '__main__':
    app.run(debug=True)
