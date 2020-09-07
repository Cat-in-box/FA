import numpy as np
import random

class Player():
    def __init__(self):
        self.identification = None
        self.symbol = None
    def color_selection(self):
        inp = input('Выберите цвет шашек, введя "Б" для белых или "Ч" для черных. (Для теста используйте Белые) -> ').upper()
        if inp == 'Б':
            Person.identification = True
            Person.symbol = '◎'
            Computer.identification = False
            Computer.symbol = '◉'
        elif inp == 'Ч':
            Person.identification = False
            Person.symbol = '◉'
            Computer.identification = True
            Computer.symbol = '◎'
        else:
            print('Такого цвета я не знаю, повторите попытку.\n', end = '')
            self.color_selection()
        
class Field():
    def __init__(self, x = None, y = None, x_new = None, y_new = None):
        self.x = x
        self.y = y
        self.x_new = x_new
        self.y_new = y_new
        self.white_storage = [0, ': ']
        self.field = np.array([[' ','A','B','C','D','E','F','G','H',' '],
                               ['8','◼','◻','◼','◻','◼','◻','◼','◻','8'],
                               ['7','◻','◼','◻','◼','◻','◼','◻','◼','7'],
                               ['6','◼','◻','◼','◻','◼','◻','◼','◻','6'],
                               ['5','◻','◼','◻','◼','◻','◼','◻','◼','5'],
                               ['4','◼','◻','◼','◻','◼','◻','◼','◻','4'],
                               ['3','◻','◼','◻','◼','◻','◼','◻','◼','3'],
                               ['2','◼','◻','◼','◻','◼','◻','◼','◻','2'],
                               ['1','◻','◼','◻','◼','◻','◼','◻','◼','1'],
                               [' ','A','B','C','D','E','F','G','H',' ']])
        self.black_storage = [0, ': ']
    def print_field(self):
        [print(a, end='') for a in self.white_storage]
        print()
        for i in np.arange(self.field.shape[0]):
            for j in np.arange(self.field.shape[1]):
                print('{:1}'.format(self.field[i][j]), end=" ")
            print()
        [print(a, end='') for a in self.black_storage]
        print()
    def put(self, printing):
        if Game_obj.flag:
            self.field[self.y][self.x] = '◎'
        else:
            self.field[self.y][self.x] = '◉'
        if printing: self.print_field()
    def move(self):
        if Game_obj.flag:
            self.field[self.y_new][self.x_new] = '◎'
        else:
            self.field[self.y_new][self.x_new] = '◉'
        self.field[self.y][self.x] = '◼'
        self.print_field()
    def eat(self):
        if Game_obj.flag:
            self.field[self.y_new][self.x_new] = '◎'
            self.black_storage[0] += 1
            self.black_storage.append('◉')
        else:
            self.field[self.y_new][self.x_new] = '◉'
            self.white_storage[0] += 1
            self.white_storage.append('◎')
        self.field[self.y][self.x] = '◼'
        self.field[self.y + (self.y_new - self.y)//2][self.x + (self.x_new - self.x)//2] = '◼'
        self.print_field()

class Checker():
    def __init__(self, x = None, y = None):
        self.x = x
        self.y = y
    def check_input(self, inp):
        if Field_obj.field[self.y][self.x] == '◻':
            return 'White'
        elif Field_obj.field[self.y][self.x] != '◼':
            return 'Taken'
        elif inp and ((Game_obj.flag and Person.identification and self.y==1) or (not Game_obj.flag and not Person.identification and self.y==8)):
            if Game_obj.flag:
                Field_obj.field[self.y][self.x] = '◇'
            else:
                Field_obj.field[self.y][self.x] = '◈'
            Game_obj.history.append(inp)
            if len(inp)==5:
                Field_obj.field[Game_obj.letters[inp[1]]][Game_obj.letters[inp[0]]] = '◼'
                Field_obj.field[Game_obj.letters[inp[1]] + (Game_obj.letters[inp[4]] - Game_obj.letters[inp[1]])//2][Game_obj.letters[inp[0]] + (Game_obj.letters[inp[3]] - Game_obj.letters[inp[0]])//2] = '◼'
            Field_obj.print_field()
            print('Вы выиграли!')
            Game_obj.Print_history()
        elif inp and ((Game_obj.flag and Computer.identification and self.y==1) or (not Game_obj.flag and not Computer.identification and self.y==8)):
            if Game_obj.flag:
                Field_obj.field[self.y][self.x] = '◇'
            else:
                Field_obj.field[self.y][self.x] = '◈'
            Game_obj.history.append(inp)
            if len(inp)==5:
                Field_obj.field[Game_obj.letters[inp[1]]][Game_obj.letters[inp[0]]] = '◼'
                Field_obj.field[Game_obj.letters[inp[1]] + (Game_obj.letters[inp[4]] - Game_obj.letters[inp[1]])//2][Game_obj.letters[inp[0]] + (Game_obj.letters[inp[3]] - Game_obj.letters[inp[0]])//2] = '◼'
            Field_obj.print_field()
            print('Вы проиграли.')
            Game_obj.Print_history()
    def check_ability(self):
        if Game_obj.flag:
            cone = '◎'
            not_cone = '◉'
            branch = -1
        else:
            cone = '◉'
            not_cone = '◎'
            branch = +1
        for i in range(len(Field_obj.field)):
            for j in range(len(Field_obj.field[i])):
                if Field_obj.field[i][j] == cone:
                    if (Field_obj.field[i+branch][j + 1] == not_cone and Field_obj.field[i + 2*branch][j + 2] == '◼'):
                        return ('Fight', i, j, i + 2*branch, j + 2)
                    elif (Field_obj.field[i+branch][j - 1] == not_cone and Field_obj.field[i + 2*branch][j - 2] == '◼'):
                        return ('Fight', i, j, i + 2*branch, j - 2)
        for i in range(len(Field_obj.field)):
            for j in range(len(Field_obj.field[i])):
                if Field_obj.field[i][j] == cone:
                    if Field_obj.field[i+branch][j + 1] == '◼':
                        return ('Quiet', i, j, i+branch, j + 1)
                    elif Field_obj.field[i+branch][j - 1] == '◼':
                        return ('Quiet', i, j, i+branch, j - 1)
        if (Game_obj.flag and Person.identification) or (not Game_obj.flag and not Person.identification):
            print('Вы проиграли.')
            Game_obj.Print_history()
        elif (Game_obj.flag and Computer.identification) or (not Game_obj.flag and not Computer.identification):
            print('Вы выиграли!')
            Game_obj.Print_history()
        return None
    def check_out_of(self):
        if (Game_obj.flag and Person.identification and Field_obj.black_storage[0]==6) or (not Game_obj.flag and not Person.identification and Field_obj.white_storage[0]==6):
            print('Вы выиграли!')
            Game_obj.Print_history()
        elif (Game_obj.flag and Computer.identification and Field_obj.black_storage[0]==6) or (not Game_obj.flag and not Computer.identification and Field_obj.white_storage[0]==6):
            print('Вы проиграли.')
            Game_obj.Print_history()
            
class Game():
    def __init__(self):
        self.letters = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 
                        '1':8, '2':7, '3':6, '4':5, '5':4, '6':3, '7':2, '8':1}
        self.not_letters = {1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G', 8:'H'} 
        self.flag = True
        self.history = []
        self.coordinates = None
        self.step = None

    def Print_history(self):
        n = 1
        l = 0
        while l < (len(self.history) - 1):
            print('\n', str(n)+'.', self.history[l], self.history[l + 1], end='')
            n+=1
            l+=2
        if len(self.history)%2==1:
            print('\n', str(n)+'.', self.history[len(self.history)-1], end='')
        print('X')
        raise SystemExit

    def arrangement(self):
        global Check_obj
        i = 0
        while i <6:
            inp = input().upper()
            try:
                self.step = (self.letters[inp[0]], self.letters[inp[1]])
            except:
                print('Кажется, вы ввели несуществующие координаты. Повторите попытку')
            else:
                Check_obj = Checker(self.step[0], self.step[1])
                if Check_obj.check_input(inp) == 'White':
                    print('На белые клетки ставить шашку нельзя! Повторите попытку')
                elif Check_obj.check_input(inp) == 'Taken':
                    print('Сюда нельзя поставить шашку! Повторите попытку')
                else:
                    Field_obj.x = self.step[0]
                    Field_obj.y = self.step[1]
                    Field_obj.put(True)
                    i+=1
    def auto_arrangement(self):
        i = 0
        while i < 6:
            self.step = (random.randint(2, 7), random.randint(2, 7))
            Check_obj = Checker(self.step[0], self.step[1])
            if (Check_obj.check_input(None) != 'White') and (Check_obj.check_input(None) != 'Taken'):
                Field_obj.x = self.step[0]
                Field_obj.y = self.step[1] 
                Field_obj.put(False)
                i+=1
        Field_obj.print_field()
    
    def process(self):
        if self.flag:
            branch = -1
        else:
            branch = +1
        inp = input('Ходите -> ').upper()
        try:
            self.coordinates = (self.letters[inp[0]], self.letters[inp[1]])
            self.step = (self.letters[inp[3]], self.letters[inp[4]])
        except:
            print('Кажется, вы ввели несуществующие координаты. Повторите попытку')
            self.process()
        else:
            Check_obj = Checker(self.coordinates[0], self.coordinates[1])
            Check_obj1 = Checker(self.step[0], self.step[1])
            if (Check_obj.check_input(inp) == 'White') or (Check_obj1.check_input(inp) == 'White'):
                print('На белые клетки ставить шашку нельзя! Повторите попытку')
                self.process()
            elif (Check_obj1.check_input(inp) == 'Taken'):
                print('Сюда нельзя поставить шашку! Повторите попытку')
                self.process()
            elif (inp[2] == '-') and (abs(self.step[0] - self.coordinates[0])==1) and ((self.step[1] - self.coordinates[1]) == branch):
                self.history.append(inp)
                Field_obj.x = self.coordinates[0]
                Field_obj.y = self.coordinates[1]
                Field_obj.x_new = self.step[0]
                Field_obj.y_new = self.step[1]
                Field_obj.move()
                Check_obj.check_input(inp)
            elif (inp[2] == ':') and (abs(self.step[0] - self.coordinates[0])==2) and ((self.step[1] - self.coordinates[1]) == 2*branch):
                self.history.append(inp)
                Field_obj.x = self.coordinates[0]
                Field_obj.y = self.coordinates[1]
                Field_obj.x_new = self.step[0]
                Field_obj.y_new = self.step[1]
                Field_obj.eat()
                Check_obj.check_input(inp)
            else:
                print('Кажется, вы сделали неверную запись. Повторите попытку')
                self.process()
    def auto_process(self, checking):
        Check_obj.x = checking[4]
        Check_obj.y = checking[3]
        if checking[0] == 'Fight':
            Check_obj.check_input(self.not_letters[checking[2]]+str(9 - checking[1])+':'+self.not_letters[checking[4]]+str(9 - checking[3]))
            self.history.append(self.not_letters[checking[2]]+str(9 - checking[1])+':'+self.not_letters[checking[4]]+str(9 - checking[3]))
            Field_obj.x = checking[2]
            Field_obj.y = checking[1]
            Field_obj.x_new = checking[4]
            Field_obj.y_new = checking[3]
            Field_obj.eat()
        elif checking[0] == 'Quiet':
            Check_obj.check_input(self.not_letters[checking[2]]+str(9 - checking[1])+'-'+self.not_letters[checking[4]]+str(9 - checking[3]))
            self.history.append(self.not_letters[checking[2]]+str(9 - checking[1])+'-'+self.not_letters[checking[4]]+str(9 - checking[3]))
            Field_obj.x = checking[2]
            Field_obj.y = checking[1]
            Field_obj.x_new = checking[4]
            Field_obj.y_new = checking[3]
            Field_obj.move()
        
    def Playing(self):
        checking = Check_obj.check_ability()
        if Person.identification == Game_obj.flag:
            if checking[0] == 'Fight':
                print('Подсказка: возможен ход с боем', self.not_letters[checking[2]]+str(9 - checking[1])+':'+self.not_letters[checking[4]]+str(9 - checking[3]))
            self.process()
            print()
        elif Computer.identification == Game_obj.flag:
            self.auto_process(checking)
        Check_obj.check_out_of()
        self.flag = not self.flag


if __name__=='__main__':
    Game_obj = Game()
    Field_obj = Field()
    Check_obj = Checker()
    Person = Player()
    Computer = Player()
    
    Field_obj.print_field()
    Person.color_selection()
    p = input('Готовые расстановки для теста (белые):\n1. Отсутствие ходов\n2. Все шашки сьедены\nДля перехода к классической игре нажмите Enter\n')
    if p == '1':
        Field_obj.field = np.array([[' ','A','B','C','D','E','F','G','H',' '],
                                     ['8','◉','◻','◉','◻','◼','◻','◼','◻','8'],
                                     ['7','◻','◉','◻','◎','◻','◼','◻','◼','7'],
                                     ['6','◉','◻','◎','◻','◎','◻','◼','◻','6'],
                                     ['5','◻','◎','◻','◎','◻','◼','◻','◼','5'],
                                     ['4','◼','◻','◼','◻','◼','◻','◼','◻','4'],
                                     ['3','◻','◼','◻','◎','◻','◼','◻','◼','3'],
                                     ['2','◼','◻','◼','◻','◼','◻','◼','◻','2'],
                                     ['1','◻','◼','◻','◼','◻','◼','◻','◼','1'],
                                     [' ','A','B','C','D','E','F','G','H',' ']])
        Field_obj.white_storage = [0, ': ']
        Field_obj.black_storage = [2, ': ', '◉', '◉']
        Field_obj.print_field()
    elif p == '2':
        Field_obj.field = np.array([[' ','A','B','C','D','E','F','G','H',' '],
                                     ['8','◼','◻','◼','◻','◼','◻','◼','◻','8'],
                                     ['7','◻','◼','◻','◎','◻','◼','◻','◼','7'],
                                     ['6','◼','◻','◎','◻','◎','◻','◼','◻','6'],
                                     ['5','◻','◎','◻','◎','◻','◼','◻','◼','5'],
                                     ['4','◼','◻','◼','◻','◉','◻','◼','◻','4'],
                                     ['3','◻','◼','◻','◎','◻','◼','◻','◼','3'],
                                     ['2','◼','◻','◼','◻','◼','◻','◼','◻','2'],
                                     ['1','◻','◼','◻','◼','◻','◼','◻','◼','1'],
                                     [' ','A','B','C','D','E','F','G','H',' ']])
        Field_obj.white_storage = [0, ': ']
        Field_obj.black_storage = [5, ': ', '◉', '◉', '◉', '◉', '◉']
        Field_obj.print_field()
    else:
        if Person.identification:
            print('Теперь вы можете расставить свои шашки. Вводите координаты, например A1. ->')
            Game_obj.arrangement()
            print()
            Game_obj.flag = False
            Game_obj.auto_arrangement()
            Game_obj.flag = True
        else:
            Game_obj.auto_arrangement()
            Game_obj.flag = False
            print('Теперь вы можете расставить свои шашки. Вводите координаты, например A1. ->')
            Game_obj.arrangement()
            Game_obj.flag = True
        
    print('Игра началась. Для тихого хода используйте конструкцию A1-B2, для хода с боем A1:C3.')
    while True:
        Game_obj.Playing()