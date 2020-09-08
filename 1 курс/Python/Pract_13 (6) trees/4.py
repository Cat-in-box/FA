import array
import copy
import timeit

class Binary_Tree:
    def __init__(self, value):
        self.root = value
        self.left = None
        self.right = None

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