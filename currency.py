
class Exceptions():
    def CurrencyTypeError(self, other):
        print("Must add currencies of the same type")

class Currency():
    def __init__(self, code, amount = 0):
        if amount == 0:
            if code[0] == '$':
                self.code = 'USD'
                self.amount = float(code[1:])
            elif code[0] == '£':
                self.code = 'GBP'
                self.amount = float(code[1:])
            elif code[0] == '€':
                self.code = 'EUR'
                self.amount = float(code[1:])
        else:
            self.code = code
            self.amount = amount

    def __eq__(self, other):
        if self.code == other.code and self.amount == other.amount:
            return True
        else:
            pass

    def __add__(self, other):
        if self.code == other.code:
            return Currency(self.code, self.amount + other.amount)
        else:
            raise Exception("CurrencyTypeError")
            pass

    def __sub__(self, other):
        if self.code == other.code:
            return Currency(self.code, self.amount - other.amount)
        else:
            raise Exception("CurrencyTypeError")
            pass

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Currency(self.code, self.amount * other)
