from app import app
from flask import render_template, request
from combinations import nChooseK

@app.route('/')
def index():
	return render_template("index.html", word_list = "", len = 0)

@app.route('/', methods=['POST'])
def my_form_post():
    n = request.form['n_input']
    k = request.form['k_input']

    if n == "" and k == "": # default values
        n = "52"
        k = "5"

    if n.isdigit() == False or k.isdigit() == False: #checks if a user enters an invalid input
        combinations_string = "ERROR: N and K must be Positive Integer values. N must be larger than K."
        error_color = 'red'
        return render_template("index.html", combinations = combinations_string, error_color = error_color)
    else:
        n = (int) (n)
        k = (int) (k)

    numbers_formatted = "You entered N: " + str(n) + " and K: " + str(k)

    if n < k:
        combinations_string = "ERROR: N must be greater than K"
        error_color = 'red'
    else:  
        combinations = nChooseK(n, k)
        combinations_string = "There are " + str(combinations) + " combinations."
        error_color = 'black'

    return render_template("index.html", users_numbers = numbers_formatted, combinations = combinations_string, error_color = error_color)

@app.route('/admin')
def admin_message():
    return 'This is the admin page'