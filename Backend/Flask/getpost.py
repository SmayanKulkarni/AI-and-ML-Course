from flask import Flask, redirect, url_for, request

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

@app.route('/submit', methods = ['POST', 'GET'])
def submit():
    total_score = 0
    if request.method == 'POST':
        datepreprocess = float(request.form['subject1'])
        DE =float(request.form['subject2'])
        ML = float(request.form['subject3'])
        DL = float(request.form['subject4'])
        total_score = 
    
        
if __name__ == '__main__':
    app.run(debug = True)