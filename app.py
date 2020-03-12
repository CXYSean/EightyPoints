from flask import Flask
from flask import render_template
import poker
import player
import random
import card

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)