from vector import Vector

v = Vector([8.218,-9.341])
w = Vector([-1.129, 2.111])

u = Vector([7.119, 8.215])
x = Vector([-8.223, 0.878])

y = 7.41
z = Vector([1.671, -1.012, -0.318])

vw = v + w
ux = u - x
zy = z.scalar(y)

print('(1) {0} + {1} = {2}\n'.format(v, w, vw))
print('(2) {0} - {1} = {2}\n'.format(u, x, ux))
print('(3) {0} * {1} = {2}\n'.format(z, y, zy))

v = Vector([-0.221, 7.437])
print('||v|| = {0}'.format(v.magnitude()))

v = Vector([8.813, -1.331, -6.247])
print('||v|| = {}'.format(v.magnitude()))

v = Vector([5.581, -2.136])
print('1/||v|| * v = {}'.format(v.direction()))

v = Vector([1.996, 3.108, -4.554])
print('1/||v|| * v = {}'.format(v.direction()))

v = Vector([7.887, 4.138])
w = Vector([-8.802, 6.776])

print('v.dot(w) = {}'.format(v.dot(w)))

v = Vector([-5.955, -4.904, -1.874])
w = Vector([-4.496, -8.755, 7.103])

print('v.dot(w) = {}'.format(v.dot(w)))

v = Vector([3.183, -7.627])
w = Vector([-2.668, 5.319])

print('v.angle(w) = {}'.format(v.angle(w)))

v = Vector([7.35, 0.221, 5.188])
w = Vector([2.751, 8.259, 3.985])

print('v.angleDeg(w) = {}'.format(v.angleDeg(w)))
