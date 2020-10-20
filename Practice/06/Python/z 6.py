import math
a = int(input())
b = int(input())
c = int(input())
if (a == 0) and (b != 0) and (c != 0):
    x = (-c) / b
    print("x = ",x)
if (a == 0) and (b == 0) and (c != 0):
    print("Нет решений")
if (a == 0) and (b != 0) and (c == 0):
    print("x = ",0)
if (a == 0) and (b == 0) and (c == 0):
    print("Нет решений")
if (a != 0) and (b == 0) and (c != 0):
    xsqrt = (-c) / a
    if (xsqrt < 0):
        print("Нет решений")
    if (xsqrt == 0):
        print("x = ",0)
    else:
        x1 = -math.sqrt(xsqrt)
        x2 = math.sqrt(xsqrt)
        print("x1 = ",x1)
        print("x2 = ",x2)
if (a != 0) and (b != 0) and (c == 0):
    x = (-b) / a
    print("x1 = ",0)
    print("x2 = ",x)
if (a != 0) and (b == 0) and (c == 0):
    print("Нет решений")
if (a != 0) and (b != 0) and (c != 0):
    d = b * b - 4 * a * c
if (d == 0):
        x = (-b) / 2 * a
        print("x = ",x)
if (d > 0):
    x1 = ((-b) + math.sqrt(d)) / 2 * a
    x2 = ((-b) - math.sqrt(d)) / 2 * a
    print("x1 = ",x1)
    print("x2 = ",x2)
else:
    print("Нет решений")

