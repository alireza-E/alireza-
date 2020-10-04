class AE:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def area(self):

        a = (self.x +self.y) * 2
        return a

    def env(self):
        a = (self.x * self.y)
        return a