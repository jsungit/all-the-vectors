# instructions
# create a vector class
# that should...
# add vectors
# scale vector
# norm or len
# dot product
# override __str__ and __repr__


class Vector:
    def __init__(self, *argv):
        self.argv = argv  # tuple

    def __add__(self, x, y):
        pass

    def myfloat(self, n):
        return float(n)

    def scale(self, scaler):
        return Vector(*[n * scaler for n in self.argv])

    def __add__(self, other):
        return Vector(*[c1 + c2 for c1, c2 in zip(self.nums, other.nums)])

    def dot(self, other):
        return sum((c1 * c2 for c1, c2 in zip(self.nums, other.nums)))

    def norm(self):
        return self.dot(self) ** 0.5

    def __str__(self):
        return "{}".format(self.argv)

    def __repr__(self):
        return self.__str__()
