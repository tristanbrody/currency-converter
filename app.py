from flask import Flask, request, render_template, redirect, session, url_for, flash
from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import CurrencyCodes, CurrencyRates
import re

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fake_key'
debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
currency = CurrencyCodes()
no_input = 'blank'

@app.route('/')
def home_page():
    invalid_amount = session.get('invalid_amount', False)
    input_vals, invalid_input = reset_session(session.get('input_vals', no_input), session.get('invalid_input', no_input));
    if invalid_input != no_input:
        for input in invalid_input:
            flash(f'{input} is not a valid currency code')
    if invalid_amount:
        flash(f'not a valid amount')
    conversion = get_conversion(input_vals, invalid_input, invalid_amount)
    symbol = currency.get_symbol(input_vals['convert-to'].upper()) if conversion != no_input else no_input
    return render_template('home.html', input_vals=input_vals, invalid_input=invalid_input, invalid_amount=invalid_amount, conversion=conversion, symbol=symbol)

@app.route('/submit')
def handle_submission():
    session['input_vals'] = request.args.to_dict()
    session['invalid_input'] = validate_currencies(session['input_vals'])
    session['invalid_amount'] = not validate_amount(session['input_vals']['amount'])
    return redirect(url_for('home_page'))

def validate_currencies(input_vals):
    invalid_input = []
    currencies = {k: v for k, v in input_vals.items() if k.startswith('convert')}
    for key, value in currencies.items():
        if currency.get_currency_name(value.upper()) == None:
            invalid_input.append(value)
    return invalid_input if invalid_input else no_input

def validate_amount(amount):
    return (re.search('^[\$£¥€]?\d+(\.\d+)?$', amount) != None)

def get_conversion(input_vals, invalid_input, invalid_amount):
    if invalid_input != no_input or invalid_amount or input_vals == no_input:
        return no_input
    if re.search('[\$£¥€]', input_vals['amount'][0]):
        input_vals['amount'] = input_vals['amount'][1:]
    convert_rate = CurrencyRates()
    return convert_rate.convert(input_vals['convert-from'].upper(), input_vals['convert-to'].upper(), float(input_vals['amount']))

def reset_session(input_vals, invalid_input):
    session['input_vals'] = no_input
    session['invalid_input'] = no_input
    session['invalid_amount'] = False
    return [input_vals, invalid_input]