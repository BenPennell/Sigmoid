import tkinter as tk

class Data:
    legend = tk.IntVar()
    legend.set(1)
    index = -1
    gType = []  # 'f' for function, 'l' for line. I'm gonna be filling this with intVars
    lookUp = [0, 1, 2, 3, 4]  # for looking up the ID of the graph to get where it was drawn
    graph_id = -1  # graph IDs
    # storage variables for the different buttons/entries to store the graph input widgets
    frames = []
    exit_buttons = []
    entries = []

    # Storing the intvars/stringvars for the checkbuttons. Only needed for plots thus far
    # index: 0 = scatter, 1 = trendline
    clickVars = [0,0,0,0,0]
