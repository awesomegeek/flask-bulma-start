import sys
from flask import Flask, render_template

DEBUG = True

app = Flask(__name__)

@app.route('/')  # noqa
def run():
    return render_template('home.html')


if __name__ == '__main__':
    app.run()
