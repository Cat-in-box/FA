#ТА САМАЯ ПРОГРАММА С ИНТЕРФЕЙСОМ
# Калькулятор дробей

Results = {} # Тут будем сохранять результаты вычислений
Result = 0

def PUSK(): # Обработка сохранения, просмотра, удаления результатов, вывода с плавающей точкой и выхода по командам save, del, to double, exit
    global Result, Results
    inp = input('Ввод ')
    
    if 'save' in inp: # Сохраняем результат
        Results[inp[inp.index(' ')+1:]]=Result
        print('save success')
        PUSK()
    elif 'del' in inp: # Удаляем результат
        Results.pop(inp[inp.index(' ')+1:])
        print('delete success')
        PUSK()
    elif inp in Results.keys(): # Если уже считали такое выражение и сохраняли, то возьмем значение оттуда
        Result=Results[inp]
        if Result[0]<Result[2]: # Обрабатываем дробный результат, если дробь правильная - выводим
            print(str(Result[0]) + '/' + str(Result[2]))
        elif Result[0]>Result[2]: # Если дробь неправильная - выделяем целую часть
            print(str(Result[0]//Result[2]) + '(' + str(Result[0]%Result[2]) + '/' + str(Result[2]) + ')')
        else: #Если числитель и знаменатель равны, то это 1
            print(1)
        PUSK()
    elif inp=='to double': # Просто выводим бесконечную десятичную дробь
        print(Result[0]/Result[2])
        PUSK()
    elif inp=='exit': # Выход
        None
    else:
        # Собственно сама основная рекурсия

        inp = inp.replace(' ', '') # Убираем пробелы
        
        for key in Results.keys(): # Если есть результат какой-то части выражения в сохраненных, заменяем им
            inp = inp.replace(key, str(Results[key][0]) + '/' + str(Results[key][2]))
        
        inp = list(inp)
        
        i = 0
        while i<(len(inp)): #Соединение цифр в многозначных числах, так как при переходе в list они разделились
            try:
                inp[i] = int(inp[i])
                inp[i+1] = int(inp[i+1])
            except:
                i+=1
            else:
                inp[i]=int(str(inp[i])+str(inp[i+1]))
                inp.pop(i+1)

        for i in range(len(inp)-1): #Замена вычитания на сложение с отрицательным числом
            if (inp[i]=='-') and (i==0):
                inp.pop(i)
                inp[i] = -inp[i]
            elif inp[i]=='-':
                inp[i] = '+'
                inp[i+1] = -inp[i+1]

        i = 0
        while i < len(inp)-5: #Перевод смешанных чисел в неправильные дроби
            if (type(inp[i])==int) and (inp[i+1]=='(') and (type(inp[i+2])==int) and (inp[i+3]=='/') and (type(inp[i+4])==int) and (inp[i+5]==')'):
                inp[i+2]+=inp[i]*inp[i+4]
                inp.pop(i)
            i += 1

        def brackets(X): #Работа со скобками
            X.remove('(')
            counter=0
            start=0
            while counter<X.count(')'):
                start = X.index(')', start,)
                counter+=1
            X.pop(start)
            return X

        def Add(A, B): #Сумма
            if (len(A)==1) and (len(B)==1):
                return [A[0]+B[0]]
            elif (len(A)==1) and (len(B)==3):
                return [A[0]*B[2]+B[0], '/', B[2]]
            elif (len(A)==3) and (len(B)==1):
                return [B[0]*A[2]+A[0], '/', A[2]]
            elif (len(A)==3) and (len(B)==3):
                return [A[0]*B[2]+B[0]*A[2], '/', A[2]*B[2]]

        def Mult(A, B): #Произведение
            if (len(A)==1) and (len(B)==1):
                return [A[0]*B[0]]
            elif (len(A)==1) and (len(B)==3):
                return [A[0]*B[0], '/', B[2]]
            elif (len(A)==3) and (len(B)==1):
                return [B[0]*A[0], '/', A[2]]
            elif (len(A)==3) and (len(B)==3):
                return [A[0]*B[0], '/', A[2]*B[2]]

        #Список чисел, которые являются простыми (делятся только на себя и 1)
        primitives = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499)

        def DivRecursion(A, B): #Поиск делителей
            for nod in primitives:
                if (A[0]%nod==0) and (B[0]%nod==0):
                    A[0]=A[0]//nod
                    B[0]=B[0]//nod
                    DivRecursion(A, B)

        def Div(A, B): #Деление
            DivRecursion(A, B)
            if len(A) == 3:
                if len(B) == 3:
                    return [A[0]*B[2], '/', A[2]*B[0]]
                else:
                    return [A[0], '/', A[2]*B[0]]
            elif len(B) == 3:
                return [A[0]*B[2], '/', B[0]]
            else:
                return [A[0], '/', B[0]]

        def F(X): # Рекурсивно разделяем список на 2 списка по приоритету действий и считаем через прописанные функции выше
            if ('+' in X) and ((('(' not in X) and (')' not in X)) or (X.index('(')>X.index('+')) or (X.index(')')<X.index('+'))):
                A = X[0:X.index('+')]
                B = X[X.index('+')+1:]
                return (Add(F(A), F(B)))
            elif ('*' in X) and ((('(' not in X) and (')' not in X)) or (X.index('(')>X.index('*')) or (X.index(')')<X.index('*'))):
                A = X[0:X.index('*')]
                B = X[X.index('*')+1:]
                return (Mult(F(A), F(B)))
            elif ('/' in X) and ('(' in X) and (')' in X) and (not ((X.count('(') == 1) and (X.count(')') == 1) and (X.index('(') == 0) and (X.index(')') == len(X)-1))):
                for i in range(len(X)):
                    if (X[i] == '/') and (X[:i].count('(') == X[:i].count(')')):
                        A = X[0:i]
                        B = X[i+1:]
                        if A[1] == B[1] and A[3] == B[3]:
                            return ([1])
                        else:
                            return (Div(F(A), F(B)))
                
            elif ('(' in X) and (')' in X):
                brackets(X)
                return(F(X))
            else:
                return X
        
        Result = F(inp) # Начала всей этой рекурсионной штуки :D
        if len(Result) > 1:
            Result = Div([Result[0]], [Result[2]]) # Если возможно, сокращаем результат

        # Еще одна обработка вывода неправильных дробей, как в интерфейсе
        if len(Result) == 1:
            print(Result[0])
        elif Result[0]<Result[2]:
            print(str(Result[0]) + '/' + str(Result[2]))
        elif Result[0]>Result[2]:
            print(str(Result[0]//Result[2]) + '(' + str(Result[0]%Result[2]) + '/' + str(Result[2]) + ')')
        else:
            print(1)
        PUSK() # Снова возвращаемся к интерфейсу
PUSK() # Старт всей программы