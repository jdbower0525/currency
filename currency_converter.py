from currency import Currency

currency_rates = {'USD': 1.0, 'EUR': 0.91, 'GBP': 0.82}


class CurrencyConverter():
    def __init__(self, currency_rates):
        self.currency_rates = currency_rates

    def convert(self, code, to):
        if self.code not in currency_rates or to not in currency_rates:
            raise UnknownCurrencyError()
        return Currency(to, self.amount *
                        (currency_rates[to]/currency_rates[self.code]))


class UnknownCurrencyError(Exception):
    pass

if __name__ == '__main__':
    main()
