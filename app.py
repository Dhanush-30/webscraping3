import numpy as np
from flask import Flask, request, jsonify, render_template
from script import scrap
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit',methods=['POST'])
def submit():

    field=request.form['Field']
    experience=request.form['Experience']
    location=request.form['Location']
    output=scrap(field=field,Experience=experience,Location=location)
    
    return output
if __name__ == "__main__":
    app.run(debug=True)
