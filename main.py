import csv
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    user_list = db.Column(db.PickleType)

    def __init__(self, username, password, user_list):
        self.username = username
        self.password = password
        self.user_list = user_list



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

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login')
def login():
    return render_template('login.html', fs=fs, bs=bs, lm=lm, vs=vs)

@app.route('/register')
def register():
    return render_template('register.html')


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
