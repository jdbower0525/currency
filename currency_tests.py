from currency import *
from currency_converter import *


def test_equals_eight_dollars():
    a = Currency('USD', 8)
    b = Currency('USD', 8)
    assert a == b

def test_does_not_equal():
    a = Currency('USD', 5)
    b = Currency('USD', 8)
    assert a != b

def test_adding_values():
    a = Currency('USD', 8)
    b = Currency('USD', 9)
    assert a + b == Currency('USD', 17)

def test_subtracting_values():
    a = Currency('USD', 9)
    b = Currency('USD', 8)
    assert a - b == Currency('USD', 1)

def test_multiplying_values():
    a = Currency('USD', 5)
    b = 5
    assert a * b == Currency('USD', 25)

def test_symbols_USD():
    a = Currency('$8')
    b = Currency('USD', 8)
    assert a == b

def test_symbols_GBP():
    a = Currency('£8')
    b = Currency('GBP', 8)
    assert a == b

def test_symbols_EUR():
    a = Currency('€8')
    b = Currency('EUR', 8)
    assert a == b

def test_basic_currency_converter():
    a = Currency('USD', 8)
    assert CurrencyConverter.convert(a, a.code, 'USD') == Currency('USD', 8)

def test_EUR_converter():
    a = Currency('USD', 2)
    to = 'EUR'
    assert CurrencyConverter.convert(a, a.code, 'EUR') == Currency('EUR', 1.82)

def test_GBP_converter():
    a = Currency('USD', 2)
    to = 'GBP'
    assert CurrencyConverter.convert(a, a.code, 'GBP') == Currency('GBP', 1.64)

def test_unknown_code_exception():
    a = Currency('USD', 2)
    to = 'CAN'
    assert CurrencyConverter.convert(a, a.code, 'CAN') == Currency('CAN', 2)




# def test_currency_code_exception():
#     a = Currency('USD', 9)
#     b = Currency('CAN', 8)
#     assert_raises(CurrencyTypeError, add, 'USD', 'CAN')

if __name__ == '__main__':
    unittest.main()
