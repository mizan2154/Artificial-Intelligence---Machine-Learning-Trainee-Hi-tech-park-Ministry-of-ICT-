#constructor cant public. always private.
#__init__ (private)
#_init_ (protected)

class rectangle:
    def __init__(self, a, b):
        self.a=5
        self.b=7
    def geta(self):
        return self.a
    def getb(self):
        return self.b
    def getArea(self):
        return self.a * self.b




