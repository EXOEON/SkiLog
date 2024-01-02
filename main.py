import pandas as pd 
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

@app.route('/')
def home():
    def table(): 
    
    # converting csv to html 
    data = pd.read_csv('sample_data.csv') 
    return render_template('table.html', tables=[data.to_html()], titles=[''])

if __name__ == '__main__':
    app.run()
