black = 0
red = 0
k = 16
z = 0
i = 0
j = 0
r = 0
n = 38
n1 = 1
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
     20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
a1 = []
a2 = []
while z > -1:
    z = int(input())
    if (-36 < z) and (z < 36):
        if k != 0:
            if (z == 1) or (z == 3) or (z == 5) or (z == 7) or (z == 9) or (z == 12) or (z == 14) or (z == 16) or (z == 18) or (z == 19) or (z == 21) or (z == 23) or (z == 25) or (z == 27) or (z == 30) or (z == 32) or (z == 34) or (z == 36):
                red = red + 1
            if (z == 2) or (z == 4) or (z == 6) or (z == 8) or (z == 10) or (z == 11) or (z == 13) or (z == 15) or (z == 17) or (z == 20) or (z == 22) or (z == 24) or (z == 26) or (z == 29) or (z == 28) or (z == 31) or (z == 33) or (z == 35):
                black = black + 1 
            for i in range(0, n):
                if (z == i):
                    a.remove(i)
                    n -= 1
                    i += 1
            for j in range(0, n1):
                a1.append(z)
            k -= 1
        else:
            for i in range(0, n):
                if (z == i):
                    a.remove(i)
                    n -= 1
                    i += 1
            for j in range(0, n1):
                a1[j] = a1[j+1]
                a1.append(z)
            if (z == 1) or (z == 3) or (z == 5) or (z == 7) or (z == 9) or (z == 12) or (z == 14) or (z == 16) or (z == 18) or (z == 19) or (z == 21) or (z == 23) or (z == 25) or (z == 27) or (z == 30) or (z == 32) or (z == 34) or (z == 36):
                red = red + 1
            if (z == 2) or (z == 4) or (z == 6) or (z == 8) or (z == 10) or (z == 11) or (z == 13) or (z == 15) or (z == 17) or (z == 20) or (z == 22) or (z == 24) or (z == 26) or (z == 29) or (z == 28) or (z == 31) or (z == 33) or (z == 35):
                black = black + 1 
            for i in range(0, n):
                if (z == i):
                    a.remove(i)
                    n -= 1
                    i += 1
            for j in range(0, n1):
                a1.append(z)
            print(a1)
            print(a)
            print(red, black)


