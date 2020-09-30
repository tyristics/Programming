g = 9.8
otv = 0
x=0 
v=0
t=0
print ("Введите x, v, t = ")
x, v, t= input().split()
otv = x + v * t + 1 / 2 * g * t * t
print (otv)
