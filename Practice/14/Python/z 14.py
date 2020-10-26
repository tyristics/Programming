n=int(input())
z=0
while n != 1:
    if n % 2 == 0:
        n = n // 2 
        z += 1
    else:
        n = n - 1
print(z)
    
