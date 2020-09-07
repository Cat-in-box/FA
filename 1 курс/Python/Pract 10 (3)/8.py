# -*- coding: utf-8 -*-

def R():
    n = int(input('Ввод числа: '))
    if n > 0:
        r = R()
        if r[0] > r[1]:
            if n > r[0] and n > r[1]:
                return (n, r[0])
            elif n < r[0] and n > r[1]:
                return (r[0], n)
            else:
                return r
        elif r[1] > r[0]:
            if n > r[0] and n > r[1]:
                return (n, r[1])
            elif n > r[0] and n < r[1]:
                return (r[1], n)
            else:
                return r
        else:
            return r
    else:
        return (1, 0)

out = R()
print(out)
if out[0]>out[1]:
    print(out[1])
else:
    print(out[0])