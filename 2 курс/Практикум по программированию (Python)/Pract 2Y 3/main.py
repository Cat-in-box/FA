import tkinter as tk
import tkinter.ttk as ttk
from toothpick import ToothPick
from tkinter import ALL

toothPicks = []
activeToothPics = []
prevActiveToothPicks = []

class mainMenu:
    
    def __init__(self, master):
        self.master = master
        self.master.geometry('800x600')
        self.frame = tk.Frame(self.master)
        self.frame.pack()
        self.prevGeneration = 0
        self.drawPicksCanvas = tk.Canvas(self.frame, width = 600, height = 600)
        self.drawPicksCanvas.grid(rowspan = 3, column = 0)
        self.spinBoxValue = tk.IntVar()
        self.spinBoxValue.set(0)
        self.spinBox = ttk.Spinbox(self.frame, from_ = 1, to = 10000, textvariable = self.spinBoxValue, command = self.updatePicks, state = 'readonly', width = 4)
        self.spinBox.grid(row = 1, column = 1, sticky = 'n') 
        self.scaleBar = tk.Scale(self.frame, from_ = 100, to = 1, orient = 'horizontal', command = lambda x: self.scale(self.scaleBar.get()*0.01), length = 100)
        self.scaleBar.set(100)
        self.scaleBar.grid(row = 1, column = 1, sticky = 's')
  
    def scale(self, scaleAmount):
        self.drawPicks()
        self.drawPicksCanvas.scale(ALL, 300, 300, scaleAmount, scaleAmount)
        
    def updatePicks(self):
        self.updatedGeneration = int(self.spinBox.get())
        if (self.updatedGeneration > self.prevGeneration):
            if (self.updatedGeneration == 1 and activeToothPics == []):
                prevActiveToothPicks.clear()
                activeToothPics.append(ToothPick((600/2, 600/2, 1)))
                prevActiveToothPicks.append(activeToothPics)
            else:
                tempPicks = []
                toothPicks.extend(activeToothPics)
                temp = activeToothPics.copy()
                prevActiveToothPicks.append(temp)
                for pick in activeToothPics:
                    if (pick.end1(toothPicks) != None):
                        tempPicks.append(pick.end1(toothPicks))
                    if (pick.end2(toothPicks) != None):
                        tempPicks.append(pick.end2(toothPicks))
                activeToothPics.clear()
                activeToothPics.extend(tempPicks)
                self.prevGeneration = self.updatedGeneration

        elif (self.updatedGeneration < self.prevGeneration):
            tempPicks = [i for i in toothPicks if i not in activeToothPics]
            toothPicks.clear()
            toothPicks.extend(tempPicks)
            activeToothPics.clear()            
            activeToothPics.extend(prevActiveToothPicks[prevActiveToothPicks.__len__()-1])
            prevActiveToothPicks.pop()
        self.prevGeneration = self.updatedGeneration
        self.scale(self.scaleBar.get()*0.01)

    def drawPicks(self):
        self.drawPicksCanvas.delete('all')
        for pick in toothPicks:
            self.drawPicksCanvas.create_line(pick.e1[0], pick.e1[1], pick.e2[0], pick.e2[1], width = 2)
        for pick in activeToothPics:
            self.drawPicksCanvas.create_line(pick.e1[0], pick.e1[1], pick.e2[0], pick.e2[1], fill = 'blue', width = 2)

def main():    
    root = tk.Tk(className = 'ToothPicks')
    root.title('ToothPicks')
    root.resizable(False, False)
    app = mainMenu(root)
    root.mainloop()

if __name__ == '__main__':
    main()