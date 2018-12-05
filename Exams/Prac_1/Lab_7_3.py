# Fraction Class


class Fraction():
    def __init__(self, *args):
        if len(args) !=2:
            print("Error")
        else:
            try:
                self.x = int(args[0])
            except:
                print("Type Error")
            else:
                try:
                    self.y = args[1]
                except:
                    print("Type Error")
        self.set_to_normal()

    def gcd(self, a, b):
        if b ==0:
            return a
        else:
            return self.gcd(b, a%b)

    def set_to_normal(self):
        common_d = self.gcd(self.x,self.y)
        self.x = self.x/common_d
        self.y = self.y/common_d

    def __repr__(self):
        return "Fraction(x={} / y={})".format(self.x, self.y)

f = Fraction(100, 50)
