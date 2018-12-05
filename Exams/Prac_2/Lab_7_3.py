class Fraction():
    def __init__(self, *args):
        if len(args) !=2:
            print("Wrong number of args: ", args)
        else:
            self.x = int(args[0])
            self.y = int(args[1])
            self.set_to_normal()

    def set_to_normal(self):
        common_div = self.gcd(self.x, self.y)
        self.x /= common_div
        self.y /= common_div

    def gcd(self,a,b):
        if b == 0:
            return a
        else:
            return self.gcd(b, a%b)

    def __str__(self):
        return "{:.0f} / {:.0f}".format(self.x, self.y)

    def __truediv__(self, other):

        x = self.x * other.y
        y = self.y * other.x
        if y == 0:
            print("error")
        print(Fraction(x,y))


f1 = Fraction(1,5)
f1 / Fraction(1,6)