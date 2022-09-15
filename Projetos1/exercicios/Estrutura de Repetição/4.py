popa = 80000
popb = 200000
anos = 0
while popa<popb:
    popa +=(popa*0.03)
    popb+= (popb*0.015)
    print (popa)
    print (popb)
    anos += 1

print (f'{anos} anos.')