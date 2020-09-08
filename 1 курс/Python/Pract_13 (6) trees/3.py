class Binary_Tree:
    def __init__(self, value):
        self.root = value
        self.left = None
        self.right = None

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

    def __str__(self):
        return '{} ({}, {})'.format(self.get_root_val(), str(self.get_left()), str(self.get_right()))
if __name__=='__main__':
    print('\nЗАДАНИЕ 3')
    # Заполнение  дерева
    Tree3 = Binary_Tree('A')
    Tree3.left = Binary_Tree('B')
    Tree3.left.left = Binary_Tree('D')
    Tree3.left.left.right = Binary_Tree('K')
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