import math
figura = input()
if figura == 'square':
    a = float(input())
    sum = a*a
elif figura == 'rectangle':
    b = float(input())
    c = float(input())
    sum = b*c
elif figura == 'circle':
    r = float(input())
    sum = math.pi*r**2
elif figura == 'triangle':
    t = float(input())
    h = float(input())
    sum = t*h/2

print(f'{ abs(sum):.3f}')