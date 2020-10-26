a=int(input())
z=0
if (a % 2 != 0) and (a % 3 != 0) and (a % 5 != 0) and (a % 7 != 0):
    z=1
if z==1:
    print("простое")
else:
    print("составное")