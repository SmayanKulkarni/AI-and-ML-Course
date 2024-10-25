from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to my Flask app!"

@app.route('/success/<int:score>')
def success(score):
    return "You have passed with a score of: " + str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "You have failed with a score of: " + str(score)

@app.route('/results/<int:marks>')
def results(marks):
    result = ""
    if marks >= 50:
        result =  'success'
    else:
        result =  'fail'
    return redirect(url_for(result , score =marks ))


if __name__ == '__main__':
    app.run(debug = True)