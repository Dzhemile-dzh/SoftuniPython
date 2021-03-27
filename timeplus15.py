chas = int(input())
min = int(input())

petna = min + 15
if petna >= 60:
    sl_chas = chas + 1
    o_min = petna % 60
    if sl_chas >= 24:
        res_chas = sl_chas%24
        sl_chas = res_chas
else:
    sl_chas = chas
    o_min = petna
if o_min < 10:
    print(f'{sl_chas}:0{o_min}')
else:
    print(f'{sl_chas}:{o_min}')