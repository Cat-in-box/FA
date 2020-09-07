import copy

class Binary_Tree:
    def __init__(self, value):
        self.root = value
        self.left = None
        self.right = None

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
    def delete_elements(self, a):
        if self.root == a:
            self._deleting(a)
        elif a<self.root:
            self.left.delete_elements(a)
        elif a>self.root:
            self.right.delete_elements(a)
    def _cleaning(self):
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