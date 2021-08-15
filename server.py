from flask import Flask
from random import randint

app = Flask(__name__)
rand_num = randint(0, 9)

def make_bold(funksiya):
    def wrapper():
        funksiya()
        return f'<b>{funksiya()}</b>'
    return wrapper


@app.route("/")
@make_bold
def hello_world():
    return '<center><h1>Guess a number between 0 and 9</h1>' \
           '<img style="height: 400px" src="https://media.giphy.com/media/h4wTo632mUgN6ObJrc/giphy.gif">' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"></center>'

@app.route(f"/<int:num>")
def bye(num):
    if num > rand_num:
        result = f'<center><h1 style="text-align:center" >Too high, try again!</h1>' \
                 f'<img style="height: 400px" src="https://media.giphy.com/media/8UGoOaR1lA1uaAN892/giphy.gif"></center>'
    elif num < rand_num:
        result = '<center><h1 style="text-align:center" >Too low, try again!</h1>' \
                 '<img style="height: 400px" src="https://media.giphy.com/media/P8WZZ0NYdbXAA/giphy.gif"></center>'
    else:
        result = '<center><h1 style="text-align:center" >You found me!</h1>' \
                 '<img style="height: 400px" src="https://media.giphy.com/media/o75ajIFH0QnQC3nCeD/giphy.gif"></center>'
    return result

if __name__ == "__main__":
    app.run(debug=True)