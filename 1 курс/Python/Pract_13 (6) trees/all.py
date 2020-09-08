import array
import copy
import timeit

class Binary_Tree:
    def __init__(self, value):
        self.root = value
        self.left = None
        self.right = None

    # Задание 2
    def _processing(self, inp):
        flag = True
        if len(inp) == 1:
            self.root = inp[0]
        else:
            for i in range(len(inp)):
                if inp[i] in ['+', '-'] and (inp[0:i].count('(') == inp[0:i].count(')')):
                    flag = False
                    self.root = inp[i]
                    self.left = Binary_Tree(None)
                    self.left._processing(inp[0:i])
                    self.right = Binary_Tree(None)
                    self.right._processing(inp[i+1:])
            if flag:
                for i in range(len(inp)):
                    if inp[i] in ['*', '/'] and (inp[0:i].count('(') == inp[0:i].count(')')):
                        flag = False
                        self.root = inp[i]
                        self.left = Binary_Tree(None)
                        self.left._processing(inp[0:i])
                        self.right = Binary_Tree(None)
                        self.right._processing(inp[i+1:])
            if flag:
                inp = inp[1:len(inp)-1]
                self._processing(inp)
    def tree_creating(self, s):
        inp = []
        for i in s:
            inp.append(i)
        i = 0
        while i < len(inp)-1:
            try:
                int(inp[i])
                int(inp[i+1])
            except:
                i+=1
            else:
                inp[i] = str(inp[i])+str(inp[i])
                inp.pop[i+1]
        self._processing(inp)
    def calculating(self):
        if self.left == None and self.right == None:
            return (self.root)
        else:
            return (str(eval(self.left.calculating()+self.root+self.right.calculating())))

    # Задание 3
    def direct_bypass(self):
        print(self.root, end='')
        if self.left!=None:
            self.left.direct_bypass()
        if self.right!=None:
            self.right.direct_bypass()
    def reverse_bypass(self):
        if self.left!=None:
            self.left.reverse_bypass()
        if self.right!=None:
            self.right.reverse_bypass()
        print(self.root, end='')
    def symmetrical_bypass(self):
        if self.left!=None:
            self.left.symmetrical_bypass()
        print(self.root, end='')
        if self.right!=None:
            self.right.symmetrical_bypass()

    # Задание 4
    def tree_from_list(self, i, arr):
            self.root = arr[i]
            if i<(len(arr)//2):
                self.left = Binary_Tree(None)
                self.right = Binary_Tree(None)
                self.left.tree_from_list(i*2+1, arr)
                self.right.tree_from_list(i*2+2, arr)
    def direct_serch(self, inp):
        if self.root == inp:
            print('Нашли', end = '')
        if self.left!=None:
            self.left.direct_serch(inp)
        if self.right!=None:
            self.right.direct_serch(inp)

    # Задание 5
    def insert_elements(self, a):
        if self.root == None:
            self.root = a
        elif a<self.root:
            if self.left == None:
                self.left = Binary_Tree(None)
            self.left.insert_elements(a)
        elif a>=self.root:
            if self.right == None:
                self.right = Binary_Tree(None)
            self.right.insert_elements(a)
    def _searching(self, a):
        if self.left == None and self.right == None:
            b = self.root
            self.root = None
            return b
        elif self.left == None:
            b = self.root
            self.root = self.right
            return b
        else:
            return self.left._searching(a)
    def _deleting(self, a):
        if self.left == None and self.right == None:
            self.root = None
        elif self.left == None or self.right == None:
            if self.left == None:
                self.root = self.right
            elif self.right == None:
                self.root = self.left
        else:
            self.root = self.right._searching(a)
    def delete_elements(self, a): # поиск удаляемого
        if self.root == a:
            self._deleting(a)
        elif a<self.root:
            self.left.delete_elements(a)
        elif a>self.root:
            self.right.delete_elements(a)
    def _cleaning(self): # чистит None(None, None)
        if self.left != None:
            if self.left.root == None and self.left.left == None and self.left.right == None:
                self.left = None
            else:
                self.left._cleaning()
        if self.right != None:
            if self.right.root == None and self.right.left == None and self.right.right == None:
                self.right = None
            else:
                self.right._cleaning()


    def insert_left(self, new_node):
        if self.left == None:
            self.left = Binary_Tree(new_node)
        else:
            t = Binary_Tree(new_node)
            t.left = self.left
            self.left = t

    def insert_right(self, new_node):
        if self.right == None:
            self.right = Binary_Tree(new_node)
        else:
            t = Binary_Tree(new_node)
            t.right = self.right
            self.right = t

    def get_right(self):
        return self.right
    def get_left(self):
        return self.left
    def set_root_val(self, obj):
        self.root = obj
    def get_root_val(self):
        return self.root

    def __str__(self):
        return '{} ({}, {})'.format(self.get_root_val(), str(self.get_left()), str(self.get_right()))

if __name__=='__main__':
    print('ЗАДАНИЕ 2')
    # 2+2
    print('1) 2+2')
    Tree2_1 = Binary_Tree(None)
    Tree2_1.tree_creating('2+2')
    print(Tree2_1)
    print(Tree2_1.calculating())
    # (2+3)*4
    print('2) (2+3)*4')
    Tree2_2 = Binary_Tree(None)
    Tree2_2.tree_creating('(2+3)*4')
    print(Tree2_2)
    print(Tree2_2.calculating())
    # (7+8)*(2-1)
    print('3) (7+8)*(2-1)')
    Tree2_3 = Binary_Tree(None)
    Tree2_3.tree_creating('(7+8)*(2-1)')
    print(Tree2_3)
    print(Tree2_3.calculating())
    # (7+8)*(2-1)+7
    print('4) (7+8)*(2-1)+7')
    Tree2_4 = Binary_Tree(None)
    Tree2_4.tree_creating('(7+8)*(2-1)+7')
    print(Tree2_4)
    print(Tree2_4.calculating())
    # (7+8)*(5-2)/(2-1)
    print('5) (7+8)*(5-2)/(2-1)')
    Tree2_5 = Binary_Tree(None)
    Tree2_5.tree_creating('(7+8)*(5-2)/(2-1)')
    print(Tree2_5)
    print(Tree2_5.calculating())

    print('\nЗАДАНИЕ 3')
    # Заполнение  дерева
    Tree3 = Binary_Tree('A')
    Tree3.left = Binary_Tree('B')
    Tree3.left.left = Binary_Tree('D')
    Tree3.left.right = Binary_Tree('E')
    Tree3.left.right.left = Binary_Tree('G')
    Tree3.right = Binary_Tree('C')
    Tree3.right.right = Binary_Tree('F')
    Tree3.right.right.left = Binary_Tree('H')
    Tree3.right.right.right = Binary_Tree('I')
    # Обходы
    print('Прямой обход:')
    Tree3.direct_bypass()
    print('\nОбратный обход:')
    Tree3.reverse_bypass()
    print('\nСимметричный обход:')
    Tree3.symmetrical_bypass()

    print('\n\nЗАДАНИЕ 4')
    # Создание
    arr = array.array('i', [81, 77, 79, 68, 10, 12, 13, 20, 15, 24, 27, 42, 33, 51, 57])
    print('Заданный массив:', arr)
    sorted_arr = sorted(copy.copy(arr))
    print('Отсортированный массив:', sorted_arr)
    Tree4 = Binary_Tree(None)
    Tree4.tree_from_list(0, arr)
    print('Дерево:', Tree4)
    # Поиск
    inp = int(input('Введите, что искать будем: '))
    if inp in arr:
        a = timeit.default_timer()
        i = arr.index(inp)
        print('Поиск в заданном массиве: Номер элемента - {}, Время - {}'.format(i+1, timeit.default_timer() - a))
        a = timeit.default_timer()
        i = sorted_arr.index(inp)
        print('Поиск в отсортированном массиве: Номер элемента - {}, Время - {}'.format(i+1, timeit.default_timer() - a))
        i = 1
        print('Поиск в дереве: Элемент - ', end = '')
        a = timeit.default_timer()
        i = Tree4.direct_serch(inp)
        print(', Время - {}'.format(timeit.default_timer() - a))
    else:
        print('Такого элемента нет')

print('\nЗАДАНИЕ 5')
# Создание
Tree5_1 = Binary_Tree(21)
Tree5_1.left = Binary_Tree(7)
Tree5_1.left.left = Binary_Tree(5)
Tree5_1.left.left.left = Binary_Tree(4)
Tree5_1.left.left.left.left = Binary_Tree(2)
Tree5_1.left.left.right = Binary_Tree(6)
Tree5_1.left.right = Binary_Tree(14)
Tree5_1.left.right.left = Binary_Tree(12)
Tree5_1.left.right.left.left = Binary_Tree(9)
Tree5_1.left.right.right = Binary_Tree(18)
Tree5_1.right = Binary_Tree(32)
Tree5_1.right.left = Binary_Tree(27)
Tree5_1.right.left.left = Binary_Tree(25)
Tree5_1.right.left.left.left = Binary_Tree(24)
Tree5_1.right.left.right = Binary_Tree(30)
Tree5_1.right.right = Binary_Tree(37)
Tree5_1.right.right.left = Binary_Tree(34)
Tree5_1.right.right.left.left = Binary_Tree(33)
Tree5_1.right.right.right = Binary_Tree(39)
print('Исходное дерево:\n', Tree5_1)
Tree5_2 = copy.deepcopy(Tree5_1)
# Вставка
insert = [38, 20, 8, 13, 47]
delete = [21]
for a in insert:
    Tree5_1.insert_elements(a)
print('Вставка элементов (38, 20, 8, 13, 47):\n', Tree5_1)
for a in delete:
    Tree5_2.delete_elements(a)
    Tree5_2._cleaning()
print('Удаление элементов (33, 14, 5, 32):\n', Tree5_2)