from flask import render_template
from app import app
from modules.calculator import add, subtract, multiply, divide

@app.route('/add/<number_1>/<number_2>')
def adding(number_1, number_2):
    result = add(int(number_1), int(number_2))
    return render_template('index.html', title='Add', result=result)

@app.route('/subtract/<number_1>/<number_2>')
def subtracting(number_1, number_2):
    result = subtract(int(number_1), int(number_2))
    return render_template('index.html', title='Subtract', result=result)

@app.route('/multiply/<number_1>/<number_2>')
def multiplying(number_1, number_2):
    result = multiply(int(number_1), int(number_2))
    return render_template('index.html', title='Multiply', result=result)

@app.route('/divide/<number_1>/<number_2>')
def division(number_1, number_2):
    result = divide(int(number_1), int(number_2))
    return render_template('index.html', title='Divide', result=result)