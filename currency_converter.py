from currency import Currency

class CurrencyConverter():
    currency_rates = {'USD':1.0, 'EUR':0.91, 'GBP':0.82}
    def __init__(self, currency_rates):
        pass

    def convert(self, from, to):
        return Currency(CurrencyConverter(to, currency.code, to, currency.amount))


# if __name__ == '__main__':
#     main()



#currency_converter.convert(Currency(1, 'USD'), 'USD') == Currency(1, 'USD')
