import tkinter

e = [1, 2, 3]
r = [2, 3, 1]
r2 = [3, 1, 2]
f = [1, 3, 2]
rf = [3, 2, 1]
r2f = [2, 1, 3]

listA = [e, r, r2, f, rf, r2f]
listB = [e, r, r2, f, rf, r2f]
Stringlist = ["e", "r", "r2", "f", "rf", "r2f"]

def comp(A1, A2):                             
    result = [0,0,0]                       
    for i in range(len(A1)):                        
        result[i] = A1[(A2[i] - 1)]           
    return result                             
                                
def findName(ResultComp):
    for i in range(len(listA)):
        if ResultComp == listA[i]:
            return Stringlist[i]
        
def printList():
    for first in listA:
        for second in listB:
            print(findName(first) + " ∘ " +  findName(second) + " = " + findName(comp(first, second)))
        
def printTable():
    print("Cayley's Table")     
    print("\te\tr\tr2\tf\trf\tr2f")
    for x in listA:
        s = (findName(x)) + "\t"
        for y in listB:
            s = s + (findName(comp(x, y))) + "\t"
        print(s)

def runDrawGrid():
    root = tkinter.Tk()
    canvas = tkinter.Canvas(root, width=400, height=400)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    drawGrid(canvas, 7)
    root.mainloop()
    
def drawGrid(canvas, size):
    xcord = 25
    ycord = 25
    cellSize = 50
    for row in range(size):
        top = row * cellSize
        bottom = top + cellSize
        for col in range(size):
            left = col * cellSize
            right = left + cellSize
            canvas.create_rectangle(left, top, right, bottom, fill = "white")
            canvas.create_rectangle(left, top, right, bottom, fill = "white")
    for element in listA:
        xcord = xcord + cellSize
        permutation = (findName(element))
        canvas.create_text(xcord, ycord, text = permutation, font = "Times 20")
    for fvalue in listA:
        ycord = ycord + cellSize
        xcord = 25
        start = (findName(fvalue))
        canvas.create_text(xcord, ycord, text = start, font = "Times 20")
        for gvalue in listB:
            xcord = xcord + cellSize
            product = (findName(comp(fvalue, gvalue)))
            canvas.create_text(xcord, ycord, text = product, font = "Times 20")

#printList()
#printTable()
runDrawGrid()


