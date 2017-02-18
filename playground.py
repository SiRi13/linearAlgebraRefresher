from vector import Vector
from line import Line
from math import *


ell1 = Line(normal_vector=Vector(['4.046', '2.836']), constant_term='1.21')
ell2 = Line(normal_vector=Vector(['10.115', '7.09']), constant_term='3.025')

print('intersetion 1:', ell1.intersection_with(ell2))
