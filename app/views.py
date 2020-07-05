from app import app
from flask import render_template, request
from combinations import nChooseK

@app.route('/')
def index():
	return render_template("index.html", word_list = "", len = 0)

@app.route('/', methods=['POST'])
def my_form_post():
    n = (int) (request.form['n_input'])
    k = (int) (request.form['k_input'])

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