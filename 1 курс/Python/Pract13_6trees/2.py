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
    Tree2_2.tree_creating('2+2*4')
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