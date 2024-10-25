from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to my Flask app!"
s
@app.route('/members')
def members():
    return "Members, welcome to my flask app"

if __name__ == '__main__':
    app.run(debug = True)