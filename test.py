import tkinter as tk
from tkinter import END
import matplotlib.pyplot as plt 

xLabel = "x-axis"
yLabel = "y-axis"
title = "Graph"
xData = []
yData = []

legend = True
lineName = ""

root = tk.Tk()
root.title("Sigmoid")

graphType = tk.StringVar(value='')
#------------------------------------------------------------------------------------------------------------The input area
#Declaring all the widgets
inputArea = tk.LabelFrame(root, text="Input datapoints, each datapoint separated by a comma (,)", padx=30)
inputArea.pack(padx=10, pady=10)
xDataE = tk.Entry(inputArea, width=50, borderwidth=5)
yDataE = tk.Entry(inputArea, width=50, borderwidth=5)
xDataL = tk.Label(inputArea, text="x-axis datapoints")
yDataL = tk.Label(inputArea, text="y-axis datapoints")
#Buttons and their functions
def getData():
    dataX = xDataE.get().split(',')
    dataY = yDataE.get().split(',')

    try:
        for x in range(len(dataX)):
            dataX[x] = float(dataX[x])
            dataY[x] = float(dataY[x])
        global xData
        global yData
        xData = dataX
        yData = dataY
    except:
        return

def clear():
    xDataE.delete(0, END)
    yDataE.delete(0, END)

clearData = tk.Button(inputArea, text="Clear", command=clear)
submitData = tk.Button(inputArea, text="Submit", command=getData)

#Displaying widgets
xDataL.grid(row=0, column=0)
xDataE.grid(row=0, column=1)
yDataL.grid(row=1, column=0)
yDataE.grid(row=1, column=1)
clearData.grid(row=0, column=2)
submitData.grid(row=1, column=2)

#------------------------------------------------------------------------------------------------------------The Name Declaring area
#declaring widgets
nameArea = tk.LabelFrame(root, text="Set Titles", padx=30)
nameArea.pack(padx=10, pady=10)
graphTitle = tk.Entry(nameArea, width=50, borderwidth=5)
graphTitleL = tk.Label(nameArea, text="Graph Title")
xAxisE = tk.Entry(nameArea, width=50, borderwidth=5)
yAxisE = tk.Entry(nameArea, width=50, borderwidth=5)
xAxisL = tk.Label(nameArea, text="y-axis label")
yAxisL = tk.Label(nameArea, text="y-axis label")
plotE = tk.Entry(nameArea, width=50, borderwidth=5)
plotL = tk.Label(nameArea, text="Line name")
#Buttons and their functions
def toggleLegend():
    global legend
    if legend == False:
        legend = True
    else:
        legend = False

legendC = tk.Checkbutton(nameArea, text="Legend", command=toggleLegend)
legendC.select()

def getNames():
    global xLabel
    global yLabel
    global title
    global lineName
    xLabel = xAxisE.get()
    yLabel = yAxisE.get()
    title = graphTitle.get()
    lineName = plotE.get()
    print(lineName)
def clearNames():
    graphTitle.delete(0, END)
    xAxisE.delete(0, END)
    yAxisE.delete(0, END)
    plotE = tk.Entry(nameArea, width=50, borderwidth=5)
    plotL = tk.Label(nameArea, text="Line name")
    plotE.grid(row=4, column=1)
    plotL.grid(row=4, column=0)
    legendC.deselect()
    global legend
    legend = False

clearNames = tk.Button(nameArea, text="Clear", command=clearNames)
submitNames = tk.Button(nameArea, text="Submit", command=getNames)

#Displaying widgets
graphTitle.grid(row=0, column=1)
xAxisE.grid(row=1, column=1)
yAxisE.grid(row=2, column=1)
graphTitleL.grid(row=0, column=0)
xAxisL.grid(row=1, column=0)
yAxisL.grid(row=2, column=0)
legendC.grid(row=3, column=1)
plotE.grid(row=4, column=1)
plotL.grid(row=4, column=0)
clearNames.grid(row=5, column=0)
submitNames.grid(row=5, column=1)

#------------------------------------------------------------------------------------------------------------The customization area
custArea = tk.LabelFrame(root, text="Graph Settings", padx=30)
custArea.pack(padx=10, pady=10)

MODES = [
    ("Regular", ""),
    ("Dashed Lines", "--"),
    ("Dots", "o"),
    ("Squares", "s"),
    ("Triangles", "^")
]
r = tk.Radiobutton(custArea, text='Regular', variable=graphType, value='')
dl = tk.Radiobutton(custArea, text='Dashed Lines', variable=graphType, value='--')
d = tk.Radiobutton(custArea, text='Dots', variable=graphType, value='o')
s = tk.Radiobutton(custArea, text='Squares', variable=graphType, value='s')
t = tk.Radiobutton(custArea, text='Triangles', variable=graphType, value='^')
r.pack()
dl.pack()
d.pack()
s.pack()
t.pack()
#---------------------------------------------------------------------------------------Drawing the graph
def drawGraph():
    plt.plot(xData, yData, str(graphType.get()), label=lineName)
    plt.xlabel(xLabel) 
    plt.ylabel(yLabel) 
    plt.title(title)
    if legend:
        plt.legend()
    plt.show()

submitGraph = tk.Button(root, text="Submit Graph", command=drawGraph)
submitGraph.pack()
root.mainloop()