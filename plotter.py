from matplotlib import pyplot

class Plotter():
    """This is Plotter. It Plots Stuff."""
    def __init__(self, **options):
        # Set optional arguments
        self.set_default_values()
        for key, value in options.items():
            if key == "title":
                self.title = value
            elif key == "xlabel":
                self.x_axis_label = value
            elif key == "ylabel":
                self.y_axis_label = value
            elif key == "color":
                self.color = value

        self.x_data = []
        self.y_data = []

        # Interactive mode on
        pyplot.ion()

        self.figure = pyplot.figure()
        self.figure.tight_layout()

        self.main_plot = self.figure.add_subplot()

        # Must assign labels after figure has been created
        pyplot.title(self.title)
        pyplot.xlabel(self.x_axis_label)
        pyplot.ylabel(self.y_axis_label)

        self.running_function, = self.main_plot.plot(self.x_data, self.y_data, self.color)

        # The visible range of the graph
        self.curr_max_x = 0
        self.curr_max_y = 0
        self.curr_min_x = 0
        self.curr_min_y = 0

    def set_default_values(self):
        """Default Optional Values Set"""
        self.title = "Plotter"
        self.x_axis_label = "X-Axis"
        self.y_axis_label = "Y-Axis"
        self.color = 'b'

    def plot(self, x_data, y_data):
        """Draws the inputed Data"""
        self.set_range(x_data, y_data)
        
        self.x_data.append(x_data)
        self.y_data.append(y_data)

        self.running_function.set_xdata(self.x_data)
        self.running_function.set_ydata(self.y_data)

        self.figure.canvas.draw()
        self.figure.canvas.flush_events()

    def set_range(self, x_data, y_data):
        """Sets the visible range of the window"""
        if(self.curr_max_x < x_data):
            self.curr_max_x = x_data

        if(self.curr_max_y < y_data):
            self.curr_max_y = y_data   

        if(self.curr_min_x > x_data):
            self.curr_min_x = x_data 

        if(self.curr_min_y > y_data):
            self.curr_min_y = y_data

        self.main_plot.set_xlim(self.curr_min_x, self.curr_max_x)
        self.main_plot.set_ylim(self.curr_min_y, self.curr_max_y)
