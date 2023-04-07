import math as m
for i in range(0,346,15):
    print(i,'=',end=' ')
    a=m.sin((m.pi)*i/180)
    print(round(a,4),end=' ')
    b=m.cos((m.pi)*i/180)
    print(round(b,4))