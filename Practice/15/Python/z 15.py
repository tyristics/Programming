qw = True
z = 0
while qw: 
    import random
    n = int(random.uniform(0, 101))
    print("Приветственное сообщение от игры")
    x = int(input())
    z = 4
    while z > 0:
        if x < n:
            print("Загаданное число больше")
            x = int(input())
            z -= 1
        if x > n:
            print("Загаданное число меньше")
            x = int(input())
            z -= 1
        if x == n:
            print("Поздравляю! Вы угадали")
            z = -1
    if z == 0:
        print("Вы проиграли. Было загадано:", n)
    z = int(input("Хотите начать сначала? (1 - ДА )"))
if z == 1:
    qw = True
else:
    qw = False
    
