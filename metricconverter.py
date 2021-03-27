res = 0.000
chislo = float(input())
vhodna = input()
izhodna = input()
if vhodna == 'mm' and izhodna == 'm':
    res = chislo*0.001
elif vhodna == 'mm' and izhodna == 'cm':
    res = chislo*0.1

elif vhodna == 'm' and izhodna == 'cm':
    res = chislo*100
elif vhodna == 'm' and izhodna == 'mm':
    res = chislo*1000

elif vhodna == 'cm' and izhodna == 'mm':
    res = chislo*10
elif vhodna == 'cm' and izhodna == 'm':
    res = chislo*0.01
print('%.3f' % res)