from flask import Flask
import random

num = random.randint(1,9)
print(num)
app = Flask(__name__)


@app.route('/')
def front_page():
    return '<h1>Guess the number from 1 to 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'

@app.route("/<int:guess>")
def guessed(guess):
    if guess < num:
        return '<h1>Too low</h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    elif guess > num:
        return '<h1>Too high</h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    else:
        return '<h1>You found me</h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'


if __name__ == "__main__":
    app.run(debug=True)
