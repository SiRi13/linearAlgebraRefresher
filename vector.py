from math import *
from decimal import Decimal, getcontext

getcontext().prec = 30

class Vector(object):

    CANNOT_NORMALIZE_ZERO_VECTOR_MSG = 'Cannot normalize the zero vector'
    NO_UNIQUE_PARALLEL_COMPONENT_MSG = 'No unique parallel component to zero vector'
    ONLY_DEFINED_IN_TWO_THREE_DIMS_MSG = 'Only defined in two dimensons'

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(self.coordinates)

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
    def normalize(self):
        try:
            return(self.scalar(Decimal('1.')/self.magnitude()))
        except ZeroDivisionError:
            raise Exception(self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG)

    def dot(self, w):
        return(round(sum([v*w for v,w in zip(self.coordinates, w.coordinates)]),3))

    def angle_with(self, w, in_degrees=False):
        try:
            u1 = self.normalize()
            u2 = w.normalize()
            angle_in_rads = acos(u1.dot(u2))
            if in_degrees:
                degrees_per_rad = 180. / pi
                return angle_in_rads * degrees_per_rad
            else:
                return angle_in_rads

        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception('Cannot compute an angle with the zero vector!')
            else:
                raise e


    def angleDeg(self, w):
        return(round(degrees(self.angle(w)), 3))

    def component_orthogonal_to(self, basis):
        try:
            projection = self.component_parallel_to(basis)
            return self - projection

        except Exception as e:
            if str(e) == self.NO_UNIQUE_PARALLEL_COMPONENT_MSG:
                raise Exception(self.NO_UNIQUE_PARALLEL_COMPONENT_MSG)
            else:
                raise e

    def component_parallel_to(self, basis):
        try:
            u = basis.normalize()
            weight = self.dot(u)
            return u.scalar(weight)
        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception(self.NO_UNIQUE_PARALLEL_COMPONENT_MSG)
            else:
                raise e

    def is_orthogonal_to(self, v, tolerance=1e-10):
        return abs(self.dot(v)) < tolerance

    def is_parallel_to(self, v):
        return ( self.is_zero() or
                v.is_zero() or
                self.angle_with(v) == 0 or
                self.angle_with(v) == pi )

    def is_zero(self, tolerance=1e-10):
        return self.magnitude() < tolerance

    def cross(self, v):
        try:
            x_1, y_1, z_1 = self.coordinates
            x_2, y_2, z_2 = v.coordinates
            new_coordinates = [ y_1*z_2 - y_2*z_1,
                               -(x_1*z_2 - x_2*z_1),
                               x-1*y_2 - x_2*y_1 ]
            return Vector(new_coordinates)
        except ValueError as e:
            msg = str(e)
            if msg == 'need more than 2 values to unpack':
                self_embedded_in_R3 = Vector(self.coordinates + ('0',))
                v_embedded_in_R3 = Vector(v.coordinates + ('0',))
                return self_embedded_in_R3.cross(v_embedded_in_R3)
            elif (msg == 'too many values to unpack' or
                  msg == 'need more than 1 value to unpack'):
                raise Exception(self.ONLY_DEFINED_IN_TWO_THREE_DIMS_MSG)
            else:
                raise e

    def area_of_triangle_with(self, v):
        return self.area_of_parallelogram_with(v) / Decimal('2.0')

    def area_of_parallelogram_with(self, v):
        cross_prod = self.cross(v)
        return cross_prod.magnitude()
