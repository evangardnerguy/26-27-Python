from math import sqrt

a = 1
b = -3
c = 2


x1 = ((-b + sqrt(b ** 2 - 4 * a * c))
    / (2 * a))
print("x1 (parenthesis) = ", x1)


x2 = (-b - sqrt(b ** 2 - 4 * a * c)) \
    / (2 * a)
print("x2 (backslash) = ", x2)
