class Graph():
    index = 0
    gType = [] #'f' for function, 'p' for plot. decides what graph we need
    function = [] #only needed for functions
    xValues = [] #only needed for plots
    yValues = [] #only needed for plots
    names = []
    plotType = []
    def __init__(self):
        self.index = 0
        self.gType = [] #'f' for function, 'p' for plot. decides what graph we need
        self.function = [] #only needed for functions
        self.xValues = [] #only needed for plots
        self.yValues = [] #only needed for plots
        self.names = []
        self.plotType = [] #only needed for plots

    def addGraph(self, gType):
        self.gType.append(gType)
        self.index += 1
    
    def addData(self, function, xVals, yVals, name, pType):
        self.function.append(function)
        self.xValues.append(xVals)
        self.yValues.append(yVals)
        self.names.append(name)
        self.plotType.append(pType)

    def getType(self, index):
        if self.gType[index] == 'f':
            return 'f'
        return 'p'
    
    def deleteGraph(self, index):
        self.gType.pop(index)
        self.function.pop(index)
        self.xValues.pop(index)
        self.yValues.pop(index)
        self.names.pop(index)
        self.plotType.pop(index)
        self.index -= 1