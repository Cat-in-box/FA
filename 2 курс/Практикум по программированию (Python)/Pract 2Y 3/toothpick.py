class ToothPick:

    def __init__(self, info):
        self.info = info
        if (info[2] == -1):    
            self.e1 = (info[0] - 20, info[1])
            self.e2 = (info[0] + 20, info[1])
        elif (info[2] == 1):
            self.e1 = (info[0], info[1] - 20)
            self.e2 = (info[0], info[1] + 20)

    def end1(self, otherPicks):
        for pick in otherPicks:
            if (pick.info != self.info):
                if (pick.e1 == self.e1 or self.e1 == pick.e2 or self.e1 == (pick.info[0], pick.info[1])):
                    return None
        return ToothPick((self.e1[0], self.e1[1], self.info[2]*(-1)))

    def end2(self, otherPicks):
        for pick in otherPicks:
            if (pick.info != self.info):
                if (pick.e1 == self.e2 or self.e2 == pick.e2 or self.e2 == (pick.info[0], pick.info[1])):
                    return None
        return ToothPick((self.e2[0], self.e2[1], self.info[2]*(-1)))