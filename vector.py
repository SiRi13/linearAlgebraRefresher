from math import *

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def __add__(self, v):
        newVec = list()
        # newVec = [x+y for x,y in zip(self.coordinates, v.coordinates)]
        for selfVal, vVal in zip(self.coordinates, v.coordinates):
            newVec.append(round(selfVal + vVal, 3))
        return(Vector(newVec))

    def __sub__(self, v):
        newVec = list()
        # newVec = [x-y for x,y in zip(self.coordinates, v.coordinates)]
        for selfVal, vVal in zip(self.coordinates, v.coordinates):
            newVec.append(round(selfVal - vVal, 3))
        return(Vector(newVec))

    def scalar(self, v):
        newVec = list()
        # newVec = [x+v for x in self.coordinates]
        for selfVal in self.coordinates:
            newVec.append(round(v * selfVal, 3))
        return(Vector(newVec))

    # length of the vector
    def magnitude(self):
        return(round(sqrt(sum([x**2 for x in self.coordinates])),3))

    # direction of the vector
    def direction(self):
        try:
            return(self.scalar(1./self.magnitude()))
        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector!')

    def dot(self, w):
        return(round(sum([v*w for v,w in zip(self.coordinates, w.coordinates)]),3))

    def angle(self, w):
        try:
            return(round(acos(self.dot(w)/(self.magnitude() * w.magnitude())), 3))
        except ZeroDivisionError:
            raise Exception('Cannot...!')

    def angleDeg(self, w):
        return(round(degrees(self.angle(w)), 3))
