from currency import Currency
from currency_converter import CurrencyConverter
from nose.tools import assert_raises


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
    assert currency_converter.convert(Currency(1, 'USD'), 'USD') == Currency(1, 'USD')





# def test_currency_code_exception():
#     a = Currency('USD', 9)
#     b = Currency('CAN', 8)
#     assert_raises(CurrencyTypeError, add, 'USD', 'CAN')

if __name__ == '__main__':
    unittest.main()
