import csv
from flask import Flask, render_template, request, redirect, url_for, session

csv_file = 'BV-Trails.csv'
data = []

with open(csv_file, 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        data.append(row)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', trails=data)

if __name__ == '__main__':
    app.run(debug=True)
