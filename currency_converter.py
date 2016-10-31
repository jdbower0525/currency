from currency import Currency

currency_rates = {'USD':1.0, 'EUR':0.91, 'GBP':0.82}

class CurrencyConverter():
    def __init__(self, currency_rates):
        pass
    def convert(self, code, to):
        if self.code == to:
            return Currency(self.code, self.amount)
        elif self.code != to:
            if self.code == 'GBP':
                if to == 'USD':
                    return Currency(to, self.amount*(currency_rates['GBP']/currency_rates['USD']))
                if to == 'EUR':
                    return Currency(to, self.amount*(currency_rates['GBP']/currency_rates['EUR']))
            elif self.code == 'EUR':
                if to == 'USD':
                    return Currency(to, self.amount*(currency_rates['EUR']/currency_rates['USD']))
                elif to == 'GBP':
                    return Currency(to, self.amount*(currency_rates['EUR']/currency_rates['GBP']))
            if self.code == 'USD':
                if to == 'EUR':
                    return Currency(to, self.amount*(currency_rates['EUR']/currency_rates['USD']))
                if to == 'GBP':
                    return Currency(to, self.amount*(currency_rates['GBP']/currency_rates['USD']))




#        return Currency(CurrencyConverter(to, currency.code, to, currency.amount))


if __name__ == '__main__':
     main()



#currency_converter.convert(Currency(1, 'USD'), 'USD') == Currency(1, 'USD')
