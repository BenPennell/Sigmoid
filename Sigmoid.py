import tkinter as tk
from tkinter import END
import matplotlib
import matplotlib.pyplot as plt
import functions as f

matplotlib.use("tkagg")

# Create window
app = tk.Tk()
app.iconbitmap("favicon.ico")
app.title("Sigmoid")

#Images
bigX = (tk.PhotoImage(file = "exit.png")).subsample(5,5)
submit = (tk.PhotoImage(file = "submit.png")).subsample(5,5)
nplot = (tk.PhotoImage(file = "Nplot.png")).subsample(10,10)
nline = (tk.PhotoImage(file = "Nline.png")).subsample(10,10)

# Storing graph information
import Data
data = Data.Data()
# -----------------------------------------------------------------------------------Graph Settings
# declaring widgets
nameArea = tk.LabelFrame(app, text="Graph Settings", bd=0, padx=30)
nameArea.pack(fill="x")
graphTitle = tk.Entry(nameArea)
graphTitleL = tk.Label(nameArea, text="Graph Title")
xAxisE = tk.Entry(nameArea)
yAxisE = tk.Entry(nameArea)
xAxisL = tk.Label(nameArea, text="x-axis label")
yAxisL = tk.Label(nameArea, text="y-axis label")

# Buttons and their functions
legendC = tk.Checkbutton(nameArea, text="Legend", variable=data.legend)
legendC.select()

# Displaying widgets
graphTitleL.grid(row=0, column=0)
graphTitle.grid(row=0, column=1)
legendC.grid(row=0, column=2)
xAxisL.grid(row=1, column=0)
xAxisE.grid(row=1, column=1)
yAxisL.grid(row=2, column=0)
yAxisE.grid(row=2, column=1)

#Frame that stores graph entry frames
graphs = tk.LabelFrame(app, bd=0, text='Graphs')
graphs.pack(fill="both", expand=1)

#----------------------------------------------------------New Graph
def new_graph(graph_type):
    #Limiting to 5 FUNCTIONS
    if data.index <= 3:
        #Incrementing the index, and working out the lookup accordingly
        data.index += 1
        data.graph_id += 1
        data.lookUp[data.index] = data.graph_id
        data.gType.append(graph_type)  # Save the graph type because drawing each type is different

        #Adding the new frame for the inputs and te delete button
        frame = tk.LabelFrame(graphs, bd=0)
        frame.pack(side="top", fill="both", expand=1)
        data.frames.append(frame)
        delete = tk.Button(frame, image=bigX, command=lambda ind=data.lookUp[data.index]: delete_graph(ind))
        delete.grid(row=0, column=2, sticky=tk.NE)
        data.exit_buttons.append(delete) # Gets put into the exit buttons area to pull from later
        if graph_type == "p": # drawing a plot
            #All the widgets
            title = tk.Entry(frame)
            x = tk.Entry(frame)
            y = tk.Entry(frame)
            l_title = tk.Label(frame, text="Graph Label:")
            l_x = tk.Label(frame, text="X-Coordinates:")
            l_y = tk.Label(frame, text="Y-Coordinates:")
            l_explanation = tk.Label(frame, text="Separate numbers by a comma")

            # the alternative interval x coordinates
            l_alternate = tk.Label(frame, text="[optional] use range and interval size")
            x_range = tk.Entry(frame, width=5)
            interval = tk.Entry(frame, width=5)
            l_x_range = tk.Label(frame, text="X range (eg. 0,5)")
            l_interval = tk.Label(frame, text="Interval size")

            l_explanation.grid(row=0, column=0, columnspan=2)
            l_title.grid(row=1, column=0)
            title.grid(row=1, column=1)
            l_x.grid(row=0, column=2)
            x.grid(row=0, column=3)
            l_y.grid(row=1, column=2)
            y.grid(row=1, column=3)

            l_alternate.grid(row=4, column=0, columnspan=4)
            l_x_range.grid(row=5, column=0)
            x_range.grid(row=5, column=1)
            l_interval.grid(row=6, column=0)
            interval.grid(row=6, column=1)

            #The "scatterplot" checkbox
            var = tk.IntVar()
            scatter = tk.Checkbutton(frame, text="Scatterplot", variable=var)
            scatter.grid(row=7, column=0)
            scatter.deselect()

            #The "trendline" checkbox
            var2 = tk.IntVar()
            trend = tk.Checkbutton(frame, text="Trendline", variable=var2)
            trend.grid(row=8, column=0, sticky=tk.W)
            trend.deselect()

            data.clickVars[data.index] = [var, var2]
            data.entries.append([title, x, y]) # Storing everything in 'data' so we can pull information from them
        elif graph_type == "l": # Drawing a line
            #Drawing all the widgets
            l_range = tk.Label(frame, text="X range (eg. 0,5):")
            l_m = tk.Label(frame, text="(slope) m:")
            l_b = tk.Label(frame, text="(y-intercept) b:")
            l_explanation = tk.Label(frame, text="Slope-intercept line: y = mx + b")
            l_explanation.grid(row=0, column=0, columnspan=2)
            l_range.grid(row=1, column=0)
            l_m.grid(row=2, column=0)
            l_b.grid(row=3, column=0)
            range = tk.Entry(frame, width=10)
            m = tk.Entry(frame, width=10)
            b = tk.Entry(frame, width=10)
            range.grid(row=1, column=1)
            m.grid(row=2, column=1)
            b.grid(row=3, column=1)

            data.entries.append([range, m, b])  # different amounts of entries needed for a line

#--------------------------------Buttons for new graphs
new_graph_buttons = tk.LabelFrame(graphs, bd=0)
new_graph_buttons.pack(side="right", fill="y")
plotButton = tk.Button(new_graph_buttons, image=nplot, command=lambda: new_graph("p"))
lineButton = tk.Button(new_graph_buttons, image=nline, command=lambda: new_graph("l"))
plotButton.pack(side="top")
lineButton.pack(side="top")

#-------------------------------------Delete Graph
def delete_graph(ind):
    # Make sure all the indexes are in order using the lookup
    data.index -= 1
    if data.index == 4:
        data.index -= 1
    ind = data.lookUp.index(ind)
    data.lookUp.pop(ind)
    data.lookUp.append(0)
    # Delete the specific graph information from the data object
    data.gType.pop(ind)
    data.exit_buttons.pop(ind)
    for e in data.entries[ind]:
        e.destroy()
    data.entries.pop(ind)
    data.frames[ind].destroy() # not sure if this is needed
    data.frames.pop(ind)

# --------------------------------------------------------------------Drawing graph
def draw_graph():
    # Setting the basic graph buttons
    settings = [graphTitle.get(), xAxisE.get(), yAxisE.get()]
    plt.xlabel(settings[1])
    plt.ylabel(settings[2])
    plt.title(settings[0])

    # loop through all the different input fields
    counter = 0
    for p in data.entries:
        x = []
        y = []
        # If it's "p" then it's a plot, so we take data from the entries as we put them in
        # 0=label, 1=xValues, 2=yValues
        if data.gType[counter] == "p":  #-----------------------------------drawing a plot
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
                data.legend.set(1)
            varsArea = data.clickVars[counter]

            if varsArea[0].get() == 1:
                plt.scatter(x, y, label=title) #Draw as a scatterplot
            else:
                plt.plot(x, y, label=title) #Draw as connected lines

            if varsArea[1].get() == 1: #Draw the trendline
                trendline = f.calculate_trendline(x, y)
                label = "Trendline for " + title + ": y = " + str(round(trendline[1], 3)) + "x + " + str(round(trendline[0], 3))
                extra = (x[0] + x[len(x) - 1]) / 10
                x1 = x[0] - extra
                x2 = x[len(x) - 1] + extra
                y1 = (trendline[1] * x1) + trendline[0]
                y2 = (trendline[1] * x2) + trendline[0]
                xp = [x1, x2]
                yp = [y1, y2]
                plt.plot(xp, yp, label=label)

        # 0=range (0-5), 1=slope(m), 2=yIntercept(b)
        if data.gType[counter] == "l":  #------------------------------------line
            rangex = p[0].get().split(',')
            x1 = float(rangex[0])
            x2 = float(rangex[1])
            m = float(p[1].get())
            b = float(p[2].get())

            #Getting the y values
            y1 = (m * x1) + b
            y2 = (m * x2) + b
            x = [x1, x2]
            y = [y1, y2]

            title = "y= " + str(m) + "x + " + str(b)
            plt.plot(x, y, label=title)
        counter += 1
    if data.legend.get() == 1:
        plt.legend()

    plt.grid()
    plt.axhline(linewidth=2, color='black')
    plt.axvline(linewidth=2, color='black')
    plt.show()

submitGraph = tk.Button(app, image=submit, command=draw_graph)
submitGraph.pack()
app.mainloop()
