import unittest
from app import app, get_conversion, validate_amount, validate_currencies
from flask import session
from forex_python.converter import CurrencyCodes, CurrencyRates

class ConverterTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_conversion(self):
        input_vals = {
            'convert-from': 'GBP',
            'convert-to': 'USD',
            'amount': '100'
        }
        invalid_amount = False
        invalid_input = 'blank'
        conversion = get_conversion(input_vals, invalid_input, invalid_amount)
        self.assertIsInstance(conversion, float)

    def test_amount(self):
        valid_amount = validate_amount('2000.34')
        invalid_amount = validate_amount('344p')
        self.assertTrue(valid_amount)
        self.assertFalse(invalid_amount)
        valid_amount = validate_amount('$32.34')
        self.assertTrue(valid_amount)

    def test_currencies(self):
        valid_currencies = {'convert-to': 'JPY', 'convert-from': 'GBP'}
        invalid_currencies = {'convert-to': 'AAAA', 'convert-from': 'BBBB'}
        self.assertIs(validate_currencies(valid_currencies), 'blank')
        self.assertEqual(validate_currencies(invalid_currencies), ['AAAA', 'BBBB'])

    def test_submit(self):
        with self.app.session_transaction() as test_session:
            params = {'convert-to': 'JPY', 'convert-from': 'USD', 'amount': '322.20'}
            response = self.app.get('/submit', query_string=params, follow_redirects=True)
            html = response.get_data(as_text=True)
            self.assertIn('converted from', html)
            params = {'convert-to': 'aaa', 'convert-from': 'USD', 'amount': '322.20'}
            response = self.app.get('/submit', query_string=params, follow_redirects=True)
            html = response.get_data(as_text=True)
            self.assertNotIn('converted from', html)
            #should return HTML without 'converted from', since the params had an invalid currency code