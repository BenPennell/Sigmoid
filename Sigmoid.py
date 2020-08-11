import tkinter as tk
from tkinter import END
import matplotlib.pyplot as plt

# Necessary storage variables
legend = True
index = -1
gType = []  # 'f' for function, 'l' for line
plotType = []
lookUp = [0, 1, 2, 3, 4]  # for looking up the ID of the graph to get where it was drawn
graph_id = 0  # graph IDs
# storage variables for the different buttons/entries to store the graph input widgets
frames = []
exit_buttons = []
entries = []

# Create windows
app = tk.Tk()
app.title("Sigmoid")
# -----------------------------------------------------------------------------------Graph Settings
# declaring widgets
nameArea = tk.LabelFrame(app, text="Graph Settings", padx=30)
nameArea.pack(fill="x")
graphTitle = tk.Entry(nameArea, width=50)
graphTitleL = tk.Label(nameArea, text="Graph Title")
xAxisE = tk.Entry(nameArea, width=50)
yAxisE = tk.Entry(nameArea, width=50)
xAxisL = tk.Label(nameArea, text="y-axis label")
yAxisL = tk.Label(nameArea, text="y-axis label")


# Buttons and their functions
def toggle_legend():
    global legend
    if not legend:
        legend = True
    else:
        legend = False


legendC = tk.Checkbutton(nameArea, text="Legend", command=toggle_legend)
legendC.select()


def clear_names():
    graphTitle.delete(0, END)
    xAxisE.delete(0, END)
    yAxisE.delete(0, END)
    legendC.deselect()
    global legend
    legend = False


clearNames = tk.Button(nameArea, text="Clear", command=clear_names)

# Displaying widgets
graphTitleL.grid(row=0, column=0)
graphTitle.grid(row=0, column=1)
xAxisL.grid(row=0, column=2)
xAxisE.grid(row=0, column=3)
yAxisL.grid(row=0, column=4)
yAxisE.grid(row=0, column=5)
legendC.grid(row=0, column=6)
clearNames.grid(row=0, column=7)

# -----------------------------------------------------------------------------------Setting data
graphs = tk.LabelFrame(app, text='Graphs')
graphs.pack(fill="both", expand=1)


# Function that creates the new input widgets and pushes the buttons over
def new_graph(graph_type):
    global index
    global gType
    global plotType
    global graph_id

    if index <= 4:
        index += 1
        print("[new graph]:" + str(index))
        lookUp[index] = graph_id
        graph_id += 1
        gType.append(graph_type)  # Save the graph type because drawing each type is different
        frame = tk.LabelFrame(graphs)
        frame.pack(side="left", fill="both", expand=1)
        frames.append(frame)
        delete = tk.Button(frame, text=" X ", bg="red", command=lambda ind=lookUp[index]: delete_graph(ind))
        delete.grid(row=0, column=2, sticky=tk.NE)
        stuff = [delete]
        if graph_type == "p":
            title = tk.Entry(frame)
            x = tk.Entry(frame)
            y = tk.Entry(frame)
            l_title = tk.Label(frame, text="Graph Label:")
            l_x = tk.Label(frame, text="X-Coordinates:")
            l_y = tk.Label(frame, text="Y-Coordinates:")
            l_explanation = tk.Label(frame, text="Separate numbers by a comma (,)")
            l_explanation.grid(row=0, column=0, columnspan=2)
            l_title.grid(row=1, column=0)
            l_x.grid(row=2, column=0)
            l_y.grid(row=3, column=0)
            title.grid(row=1, column=1)
            x.grid(row=2, column=1)
            y.grid(row=3, column=1)
            entry = [title, x, y]  # So basically we store the entries in an array to pull data from them
            entries.append(entry)
        elif graph_type == "l":
            l_x1 = tk.Label(frame, text="(x coordinate) Range from:")
            l_x2 = tk.Label(frame, text="(x coordinate) To:")
            l_m = tk.Label(frame, text="(slope) m:")
            l_b = tk.Label(frame, text="(y-intercept) b:")
            l_explanation = tk.Label(frame, text="Slope-intercept line: y = mx + b")
            l_explanation.grid(row=0, column=0, columnspan=2)
            l_x1.grid(row=1, column=0)
            l_x2.grid(row=2, column=0)
            l_m.grid(row=3, column=0)
            l_b.grid(row=4, column=0)
            x1 = tk.Entry(frame, width=10)
            x2 = tk.Entry(frame, width=10)
            m = tk.Entry(frame, width=10)
            b = tk.Entry(frame, width=10)
            x1.grid(row=1, column=1)
            x2.grid(row=2, column=1)
            m.grid(row=3, column=1)
            b.grid(row=4, column=1)
            entry = [x1, x2, m, b]  # different amounts of entries needed for a line
            entries.append(entry)
        exit_buttons.append(stuff)


# Buttons for different graphs
new_graph_buttons = tk.LabelFrame(graphs, text='')
new_graph_buttons.pack(side="right")
plotButton = tk.Button(new_graph_buttons, text="+ new plot", bg="green", command=lambda: new_graph("p"))
lineButton = tk.Button(new_graph_buttons, text="+ new line", bg="Green", command=lambda: new_graph("l"))
plotButton.pack()
lineButton.pack()


def delete_graph(ind):
    global index
    global gType
    index -= 1
    if index == 4:
        index -= 1

    ind = lookUp.index(ind)
    lookUp.pop(ind)
    lookUp.append(0)
    print("[Delete Graph]:" + str(index) + ", " + str(ind))
    # Delete the specific graph
    gType.pop(ind)
    # plotType.pop(ind)
    for l in exit_buttons[ind]:
        l.destroy()
    exit_buttons.pop(ind)
    for e in entries[ind]:
        e.destroy()
    entries.pop(ind)
    frames[ind].destroy()
    frames.pop(ind)


# ---------------------------------------------------------------------------------The submit button
def draw_graph():
    global gType
    global legend
    # Setting the basic graph buttons
    data = [graphTitle.get(), xAxisE.get(), yAxisE.get()]
    plt.xlabel(data[1])
    plt.ylabel(data[2])
    plt.title(data[0])

    # loop through all the different input fields
    counter = 0
    for p in entries:
        x = []
        y = []
        title = ''
        # If it's "p" then it's a plot, so we take data from the entries as we put them in
        # 0=label, 1=xValues, 2=yValues
        if gType[counter] == "p":
            x = p[1].get().split(',')
            y = p[2].get().split(',')
            if len(x) == len(y):
                for ind in range(len(x)):
                    x[ind] = float(x[ind])
                    y[ind] = float(y[ind])
                title = str(p[0].get())
            else:
                x = []
                y = []
                title = "unequal amount of x and y values"
                legend = True
        # 0=StartingX, 1=FinalX, 2=slope(m), 3=yIntercept(b)
        if gType[counter] == "l":
            x1 = float(p[0].get())
            x2 = float(p[1].get())
            m = float(p[2].get())
            b = float(p[3].get())

            # setting a series of x and y values to draw, I arbitrarily chose 10 points but we could do it with 2
            step = (x2 - x1) / 10
            for i in range(10):
                x_val = x1 + (i * step)
                y_val = (m * x_val) + b
                x.append(x_val)
                y.append(y_val)
            title = "y= " + str(m) + "x + " + str(b)
        plt.plot(x, y, label=title)
        counter += 1
    if legend:
        plt.legend()
    plt.show()


submitGraph = tk.Button(app, text="Draw my graph!", bg="blue", height=2, command=draw_graph)
submitGraph.pack()

app.mainloop()
