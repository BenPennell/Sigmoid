import tkinter as tk
from tkinter import END
import matplotlib.pyplot as plt 
from graphObject import Graph

legend = True

sigmoid = Graph()

app = tk.Tk()
app.title("Sigmoid")
#------------------------------------------------------------------------------------------------------------Graph Settings
#declaring widgets
nameArea = tk.LabelFrame(app, text="Graph Settings", padx=30)
nameArea.pack(padx=10, pady=10, fill="x")
graphTitle = tk.Entry(nameArea, width=50, borderwidth=5)
graphTitleL = tk.Label(nameArea, text="Graph Title")
xAxisE = tk.Entry(nameArea, width=50, borderwidth=5)
yAxisE = tk.Entry(nameArea, width=50, borderwidth=5)
xAxisL = tk.Label(nameArea, text="y-axis label")
yAxisL = tk.Label(nameArea, text="y-axis label")
#Buttons and their functions
def toggleLegend():
    global legend
    if legend == False:
        legend = True
    else:
        legend = False

legendC = tk.Checkbutton(nameArea, text="Legend", command=toggleLegend)
legendC.select()

def clearNames():
    graphTitle.delete(0, END)
    xAxisE.delete(0, END)
    yAxisE.delete(0, END)
    legendC.deselect()
    global legend
    legend = False

clearNames = tk.Button(nameArea, text="Clear", command=clearNames)

#Displaying widgets
graphTitleL.grid(row=0, column=0)
graphTitle.grid(row=0, column=1)
xAxisL.grid(row=0, column=2)
xAxisE.grid(row=0, column=3)
yAxisL.grid(row=0, column=4)
yAxisE.grid(row=0, column=5)
legendC.grid(row=0, column=6)
clearNames.grid(row=0, column=7)


#------------------------------------------------------------------------------------------------------------Graphs
graphs = tk.LabelFrame(app, text='')
graphs.pack(fill="x")

frames = []
labels = []
entrys = []

def newPlot():
    if Graph.index <= 4:
        Graph.addGraph(Graph, "p")
        frame = tk.LabelFrame(graphs)
        frame.grid(column=Graph.index - 1, row=0)
        frames.append(frame)
        title = tk.Entry(frame)
        x = tk.Entry(frame)
        y = tk.Entry(frame)
        title.pack()
        x.pack()
        y.pack()
        entry = [title, x, y]
        entrys.append(entry)
        plotButton.grid(column=Graph.index, row=0, sticky=tk.W)
        formulaButton.grid(column=Graph.index, row=1, sticky=tk.W)
def newGraph():
    if Graph.index <= 4:
        Graph.addGraph(Graph, "f")
        frame = tk.LabelFrame(graphs)
        frame.grid(column=Graph.index - 1, row=0)
        frames.append(frame)
        label = tk.Label(frames[Graph.index-1], text='This is a graph thing')
        label.pack()
        labels.append(label)
        plotButton.grid(column=Graph.index, row=0, sticky=tk.W)
        formulaButton.grid(column=Graph.index, row=1, sticky=tk.W)

plotButton = tk.Button(graphs, text="+ new plot", bg="green", command=newPlot)
formulaButton = tk.Button(graphs, text="+ new graph", bg="Green", command=newGraph)
plotButton.grid(column=0, row=0, sticky=tk.W)
formulaButton.grid(column=0, row=1, sticky=tk.W)


#------------------------------------------------------------------------------------------------------------The submit button
def drawGraph():
    data = setData()
    plt.xlabel(data[1]) 
    plt.ylabel(data[2]) 
    plt.title(data[0])
    for p in entrys:
        x = p[1].get().split(',')
        y = p[2].get().split(',')
        try:
            for ind in range(len(x)):
                x[ind] = float(x[ind])
                y[ind] = float(y[ind])
        except:
            print("fuck")

        plt.plot(x, y, label=str(p[0].get()))
    if legend:
        plt.legend()
    plt.show()

def setData():
    data = [graphTitle.get(), xAxisE.get(), yAxisE.get()]
    return data
submitGraph = tk.Button(app, text="Submit Graph", command=drawGraph)
submitGraph.pack()

app.mainloop()
