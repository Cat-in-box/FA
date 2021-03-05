# Текстовый калькулятор

perevod1 = {'один': '1', 'два': '2', 'три': '3', 'четыре': '4', 'пять': '5', 
            'шесть': '6', 'семь': '7', 'восемь': '8', 'девять': '9', 'десять': '10', 
            'одиннадцать': '11', 'двенадцать': '12', 'тринадцать': '13', 'четырнадцать': '14', 
            'пятнадцать': '15', 'шестнадцать': '16', 'семнадцать': '17', 'восемнадцать': '18', 'девятнадцать': '19', 
            'двадцать': '20', 'тридцать': '30', 'сорок': '40', 'пятьдесят': '50', 
            'шестьдесят': '60', 'семьдесят': '70', 'восемьдесят': '80', 'девяносто': '90', 
            'плюс': '+', 'минус': '-', 'умножить на': '*', 'разделить на': '/', 
            'скобка открывается': '(', 'скобка закрывается': ')', 
            'целых': '(', 'целая': '(', 'одна': '1', 'две': '2', 
            'первых': '1 )', 'вторых': '2 )', 'третьих': '3 )', 'четвертых': '4 )', 'пятых': '5 )', 
            'шестых': '6 )', 'седьмых': '7 )', 'восьмых': '8 )', 'девятых': '9 )', 'десятых': '10 )', 
            'одиннадцатых': '11 )', 'двенадцатых': '12 )', 'тринадцатых': '13 )', 'четырнадцатых': '14 )', 
            'пятнадцатых': '15 )', 'шестнадцатых': '16 )', 'семнадцатых': '17 )', 'восемнадцатых': '18 )', 'девятнадцатых': '19 )', 
            'двадцатых': '20 )', 'тридцатых': '30 )', 'сороковых': '40 )', 'пятидесятых': '50 )', 
            'шестидесятых': '60 )', 'семидесятых': '70 )', 'восьмидесятых': '80 )', 'девяностых': '90 )', 
            'вторая': '2 )', 'третья': '3 )', 'четвертая': '4 )', 'пятая': '5 )', 
            'шестая': '6 )', 'седьмая': '7 )', 'восьмая': '8 )', 'девятая': '9 )', 'десятая': '10 )', 
            'одиннадцатая': '11 )', 'двенадцатая': '12 )', 'тринадцатая': '13 )', 'четырнадцатая': '14 )', 
            'пятнадцатая': '15 )', 'шестнадцатая': '16 )', 'семнадцатая': '17 )', 'восемнадцатая': '18 )', 'девятнадцатая': '19 )', 
            'двадцатая': '20 )', 'тридцатая': '30 )', 'сороковая': '40 )', 'пятидесятая': '50 )', 
            'шестидесятая': '60 )', 'семидесятая': '70 )', 'восьмидесятая': '80 )', 'девяностая': '90 )'}

perevod = {1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 
           6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять', 10: 'десять', 
           11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать', 14: 'четырнадцать', 
           15: 'пятнадцать', 16: 'шестнадцать', 17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать', 
           20: 'двадцать', 30: 'тридцать', 40: 'сорок', 50: 'пятьдесят', 
           60: 'шестьдесят', 70: 'семьдесят', 80: 'восемьдесят', 90: 'девяносто'}

chisliteli = {1: 'одна', 2: 'две', 3: 'три', 4: 'четыре', 5: 'пять', 
              6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять', 10: 'десять', 
              11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать', 14: 'четырнадцать', 
              15: 'пятнадцать', 16: 'шестнадцать', 17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать', 
              20: 'двадцать', 30: 'тридцать', 40: 'сорок', 50: 'пятьдесят', 
              60: 'шестьдесят', 70: 'семьдесят', 80: 'восемьдесят', 90: 'девяносто'}

znamenateli = {1: 'первых', 2: 'вторых', 3: 'третьих', 4: 'четвертых', 5: 'пятых', 
               6: 'шестых', 7: 'седьмых', 8: 'восьмых', 9: 'девятых', 10: 'десятых', 
               11: 'одиннадцатых', 12: 'двенадцатых', 13: 'тринадцатых', 14: 'четырнадцатых', 
               15: 'пятнадцатых', 16: 'шестнадцатых', 17: 'семнадцатых', 18: 'восемнадцатых', 19: 'девятнадцатых', 
               20: 'двадцатых', 30: 'тридцатых', 40: 'сороковых', 50: 'пятидесятых', 
               60: 'шестидесятых', 70: 'семидесятых', 80: 'восьмидесятых', 90: 'девяностых'}

znamenateli1 = {1: 'первая', 2: 'вторая', 3: 'третьая', 4: 'четвертая', 5: 'пятая', 
               6: 'шестая', 7: 'седьмая', 8: 'восьмая', 9: 'девятая', 10: 'десятая', 
               11: 'одиннадцатая', 12: 'двенадцатая', 13: 'тринадцатая', 14: 'четырнадцатая', 
               15: 'пятнадцатая', 16: 'шестнадцатая', 17: 'семнадцатая', 18: 'восемнадцатая', 19: 'девятнадцатая', 
               20: 'двадцатая', 30: 'тридцатая', 40: 'сороковая', 50: 'пятидесятая', 
               60: 'шестидесятая', 70: 'семидесятая', 80: 'восьмидесятая', 90: 'девяностая'}

#ТА САМАЯ ПРОГРАММА С ИНТЕРФЕЙСОМ

Results = {}
Result = 0

def PUSK():
    global Result, Results, inp
            

    for i in range(len(inp)-1): #Замена вычитания на сложение с отрицательным числом
        if (inp[i]=='-') and (i==0):
            inp.pop(i)
            inp[i] = -inp[i]
        elif inp[i]=='-':
            inp[i] = '+'
            inp[i+1] = -inp[i+1]
    
    i = 0
    schetchik_dliny_spiska = len(inp)-5
    while (i < schetchik_dliny_spiska): #Перевод смешанных чисел в неправильные дроби
        print('zashli')
        if (type(inp[i])==int):
            if (inp[i+1]=='('):
                if (type(inp[i+2])==int):
                    if (inp[i+3]=='/'):
                        if(type(inp[i+4])==int):
                            if (inp[i+5]==')'):
                                inp[i+2]+=inp[i]*inp[i+4]
                                inp.pop(i)
                                inp.pop(i)
                                inp.pop(i+3)
        i+=1
        schetchik_dliny_spiska = len(inp)-5
    print(inp)

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

    primitives = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499)

    def DivRecursion(A, B): #Поиск делителей
        for nod in primitives:
            if (A[0]%nod==0) and (B[0]%nod==0):
                A[0]=A[0]//nod
                B[0]=B[0]//nod
                DivRecursion(A, B)

    def Div(A, B): #Деление
        DivRecursion(A, B)
        return [A[0], '/', B[0]]

    def F(X):
        if ('+' in X) and ((('(' not in X) and (')' not in X)) or (X.index('(')>X.index('+')) or (X.index(')')<X.index('+'))):
            A = X[0:X.index('+')]
            B = X[X.index('+')+1:]
            return (Add(F(A), F(B)))
        elif ('*' in X) and ((('(' not in X) and (')' not in X)) or (X.index('(')>X.index('*')) or (X.index(')')<X.index('*'))):
            A = X[0:X.index('*')]
            B = X[X.index('*')+1:]
            return (Mult(F(A), F(B)))
        elif ('/' in X) and ((('(' not in X) and (')' not in X)) or (X.index('(')>X.index('/')) or (X.index(')')<X.index('/'))):
            A = X[0:X.index('/')]
            B = X[X.index('/')+1:]
            return (Div(F(A), F(B)))
        elif ('(' in X) and (')' in X):
            brackets(X)
            return(F(X))
        else:
            return X
        
    Result = F(inp)
    if len(Result)>1:
        Result = Div([Result[0]], [Result[2]])
        
        
def Calc():
    global Result, Results, inp, perevod
    flag = True
    
    for i in perevod1.keys():
        inp = inp.replace(i, perevod1[i])
    
    print(inp)
    
    inp = inp.split(' ')
    
    for i in range(len(inp)):
        inp[i] = inp[i].replace(' ', '')
        
    for i in range(len(inp)-1):
        try:
            if int(inp[i])<int(inp[i+1]):
                inp.insert(i+1, '/')
        except:
           None 
    
    i = 0
    while i<(len(inp)): #Соединение цифр в многозначных числах
        try:
            inp[i] = int(inp[i])
            inp[i+1] = int(inp[i+1])
        except:
            i+=1
        else:
            inp[i]=inp[i]+inp[i+1]
            inp.pop(i+1)
            
    i = 0
    while i<(len(inp)-1): #Добавление скобки в дробях, если её нет
        if (inp[i]!='(') and (type(inp[i])==int) and (inp[i+1]=='/'):
            inp.insert(i, '(')
            i+=2
        else:
            i+=1
            
    i = 0
    while i<(len(inp)-1):
        if (inp[i]=='(') and (inp[i+1]=='('):
            inp.pop(i)
        i+=1
    
    print(inp)
    
    PUSK()
    
    '''
    except:
        print('Ой, что-то пошло не так. Проверьте введенное выражение!')
    '''
    
    print(Result)
    
    #Вывод
    
    if len(Result)==1:
        if Result[0]<20:
            print(perevod[Result[0]])
        elif (19<Result[0]) and (Result[0]<100):
            print(perevod[Result[0] - Result[0]%10], perevod[Result[0]%10])
        else:
            print('Получилось число больше 99, мы не можем сконвертировать его в слова((')
            
    elif Result[0]<Result[2]:
        if Result[0]<20:
            print(chisliteli[Result[0]], end = ' ')
        elif (19<Result[0]) and (Result[0]<100):
            print(chisliteli[Result[0] - Result[0]%10], chisliteli[Result[0]%10], end = ' ')
        else:
            print('[Получилось число больше 99, мы не можем сконвертировать его в слова((]', end = ' ')
        if Result[0]==1:
            if Result[2]<20:
                print(znamenateli1[Result[2]])
            elif (19<Result[2]) and (Result[2]<100):
                print(perevod[Result[2] - Result[2]%10], znamenateli1[Result[2]%10])
            else:
                print('[Получилось число больше 99, мы не можем сконвертировать его в слова((]')
        else:
            if Result[2]<20:
                print(znamenateli[Result[2]])
            elif (19<Result[2]) and (Result[2]<100):
                print(perevod[Result[2] - Result[2]%10], znamenateli[Result[2]%10])
            else:
                print('[Получилось число больше 99, мы не можем сконвертировать его в слова((]')

    elif Result[0]>Result[2]:
        Result_smesh = []
        Result_smesh.append(Result[0]//Result[2])
        Result_smesh.append(Result[0]%Result[2])
        Result_smesh.append(Result[2])
        if Result_smesh[0]==1:
            print('одна целая', end = ' ')
        elif Result_smesh[0]<20:
            print(perevod[Result_smesh[0]], 'целых', end = ' ')
        elif (19<Result_smesh[0]) and (Result_smesh[0]<100):
            print(perevod[Result_smesh[0] - Result_smesh[0]%10], perevod[Result_smesh[0]%10], 'целых', end = ' ')
        else:
            print(['Получилось число больше 99, мы не можем сконвертировать его в слова(('], 'целых', end = ' ')
        if Result_smesh[1]<20:
            print(chisliteli[Result_smesh[1]], end = ' ')
        elif (19<Result_smesh[1]) and (Result_smesh[1]<100):
            print(chisliteli[Result_smesh[1] - Result_smesh[1]%10], chisliteli[Result_smesh[1]%10], end = ' ')
        else:
            print('[Получилось число больше 99, мы не можем сконвертировать его в слова((]', end = ' ')
        if Result_smesh[1]==1:
            if Result_smesh[2]<20:
                print(znamenateli1[Result[2]])
            elif (19<Result_smesh[2]) and (Result_smesh[2]<100):
                print(perevod[Result_smesh[2] - Result_smesh[2]%10], znamenateli1[Result_smesh[2]%10])
            else:
                print('[Получилось число больше 99, мы не можем сконвертировать его в слова((]')
        else:
            if Result_smesh[2]<20:
                print(znamenateli[Result[2]])
            elif (19<Result_smesh[2]) and (Result_smesh[2]<100):
                print(perevod[Result_smesh[2] - Result_smesh[2]%10], znamenateli[Result_smesh[2]%10])
            else:
                print('[Получилось число больше 99, мы не можем сконвертировать его в слова((]')
        
    else:
        print('один')
    
inp = input('Ввод ')
try:
    Calc()
except:
    None

'''одна целая две седьмых плюс две целых пять седьмых'''