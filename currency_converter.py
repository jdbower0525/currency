from currency import Currency

currency_rates = {'USD':1.0, 'EUR':0.91, 'GBP':0.82}

class UnknownCurrencyError(Exception):
    pass

class CurrencyConverter():
    def __init__(self, currency_rates):
        pass
    def convert(self, code, to):
        if self.code not in currency_rates or to not in currency_rates:
            raise Exception("UnknownCurrencyError")
        return Currency(to, self.amount * (currency_rates[to]/currency_rates[self.code]))



#        return Currency(CurrencyConverter(to, currency.code, to, currency.amount))


if __name__ == '__main__':
     main()



#currency_converter.convert(Currency(1, 'USD'), 'USD') == Currency(1, 'USD')
