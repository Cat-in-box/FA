# -*- coding: utf-8 -*-
s = input('Введите список через пробел ')
s = list(s.split(' '))
k = 0
for i in range(len(s)):
    s1 = s.copy()
    del s1[i]
    for j in range(len(s1)):
        s2 = s1.copy()
        del s2[j]
        s3 = s2.copy()
        s3.sort()
        if s2 == s3:
            k+=1
if k>0: 
    print("Можно")
else: print("Нельзя")