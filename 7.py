from unittest import result


class Fraction:
    def __init__(self, s,m):
        self.soorat = s
        self.makhraj = m

    def sum(self, mehman):
        result = Fraction(None, None)
        result.soorat = (self.soorat * mehman.soorat) + (self.makhraj * mehman.makhraj)
        result.makhraj = self.makhraj * mehman.makhraj
        return result

    def mul(self, mehman):
        result = Fraction(None, None)
        result.soorat = self.soorat * mehman.soorat
        result.makhraj = self.makhraj * mehman.makhraj
        return result

    def sub(self, mehman):
        result = Fraction(None, None)
        result.soorat = (self.makhraj * mehman.soorat) - (self.soorat * mehman.makhraj)
        result.makhraj = self.makhraj * mehman.makhraj
        return result

    def div(self, mehman):
        result = Fraction(None, None)
        result.soorat = self.makhraj * mehman.soorat
        result.makhraj = self.soorat * mehman.makhraj
        return result
    
    def show(self):
        print(self.soorat,'/', self.makhraj)

a = Fraction(8,9)
b = Fraction(3,4)

a.show()
b.show()
c = b.div(a)
c.show()