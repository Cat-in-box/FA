# -*- coding: utf-8 -*-
s = list(input('Введите предложение '))
a = list('itmathrepetitor')
b = list('silence')
c = list()
i = 0
while i < (len(s)):
    j = 0
    k = 0
    f = True
    while f:
        try:
            if k==15:
                c.extend(b)
                i+=14
                f = False
            elif s[i+j]==a[j]:
                j+=1
                k+=1
            else:
                c.append(s[i])
                f = False
        except:
            c.append(s[i])
    i+=1
for i in range (len(c)):
    print(c[i], end = "")