def tree_creating(self, inp):
        print(inp)
        print(self)
        if inp[0] == '(':
            inp = inp[1:]
            if inp[0:4]!=None:
                self.left = Binary_Tree(inp[0])
                inp = inp[1:]
                self.tree_creating(inp)
            else:
                inp = inp[4:]
        if inp[0] == ',':
            inp = inp[1:]
            if inp[0:4]!=None:
                self.right = Binary_Tree(inp[0])
                inp = inp[1:]
                self.tree_creating(inp)
            else:
                inp = inp[4:]
        if inp[0] == ')':
            inp = inp[1:]

if len(inp) != 1:
            while not (inp[0] == '(' and inp[len(inp)-1] == ')'):
                for i in range(len(inp)):
                    if inp[i] in ['+', '-'] and ('(' not in inp[0:i] and ')' not in inp[i+1:]):
                        self.root = inp[i]
                        self.left = Binary_Tree(None)
                        self.left._processing(inp[0:i])
                        self.right = Binary_Tree(None)
                        self.right._processing(inp[i+1:])
                for i in range(len(inp)):
                    if inp[i] in ['*', '/'] and ('(' not in inp[0:i] and ')' not in inp[i+1:]):
                        self.root = inp[i]
                        self.left = Binary_Tree(None)
                        self.left._processing(inp[0:i])
                        self.right = Binary_Tree(None)
                        self.right._processing(inp[i+1:])
            inp = inp[1:len(inp)-1]
            for i in range(len(inp)):
                if inp[i] in ['+', '-'] and ('(' not in inp[0:i] and ')' not in inp[i+1:]):
                    self.root = inp[i]
                    self.left = Binary_Tree(None)
                    self.left._processing(inp[0:i])
                    self.right = Binary_Tree(None)
                    self.right._processing(inp[i+1:])
            for i in range(len(inp)):
                if inp[i] in ['*', '/'] and ('(' not in inp[0:i] and ')' not in inp[i+1:]):
                    self.root = inp[i]
                    self.left = Binary_Tree(None)
                    self.left._processing(inp[0:i])
                    self.right = Binary_Tree(None)
                    self.right._processing(inp[i+1:])
        else:
            self.root = inp[0]