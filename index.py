from flask import Flask
import random
from flask import render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("main_home.html")


@app.route('/<move>')
def hello(move):
    moves = ['rock', 'paper', 'scissor']
    computer_move = moves[random.randint(0, 2)]
    # player_move = True
    played = move
    return render_template("home.html", content={"a": played , "b":computer_move })



if __name__ == '__main__':
   app.run(debug=True)