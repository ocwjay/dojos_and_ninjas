from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return 'Invalid URL.'

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojo():
    dojos = Dojo.get_all_dojos()
    return render_template('dojo.html', all_dojos = dojos)

@app.route('/new_dojo_submission', methods=['POST'])
def new_dojo_submission():
    data = {
        'name' : request.form['dojoname']
    }
    Dojo.create_dojo(data)
    return redirect('/dojos')

@app.route('/new_ninja_submission', methods=['POST'])
def new_ninja_submission():
    data = {
        'fname' : request.form['fname'],
        'lname' : request.form['lname'],
        'age' : request.form['age'],
        'dojo_id' : request.form['dojoselect']
    }
    Ninja.create_ninja(data)
    return redirect('/')

@app.route('/ninjas')
def ninja():
    dojos = Dojo.get_all_dojos()
    return render_template('ninja.html', all_dojos = dojos)

@app.route('/dojos/<int:id>')
def dojo_show(id):
    data = {
        'id' : id
    }
    dojo = Dojo.get_dojo_with_ninjas(data)
    return render_template('dojo_show.html', one_dojo = dojo)
