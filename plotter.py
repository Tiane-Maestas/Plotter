from matplotlib import pyplot
import numpy

class Plotter():
    """This is Plotter"""
    def __init__(self):

        # self.x_data = numpy.linspace(0, 10*numpy.pi, 100)
        # self.y_data = numpy.sin(self.x_data)
        self.x_data = [0.0]
        self.y_data = [0.0]

        pyplot.ion()
        self.figure = pyplot.figure()
        self.main_plot = self.figure.add_subplot()
        self.running_function, = self.main_plot.plot(self.x_data, self.y_data, 'r-')
        self.figure.tight_layout()

        self.curr_max_x = 0
        self.curr_max_y = 0

        self.curr_min_x = 0
        self.curr_min_y = 0

    def plot(self, x_data, y_data):
        """Draw"""
        if(self.curr_max_x < x_data):
            self.curr_max_x = x_data

        if(self.curr_max_y < y_data):
            self.curr_max_y = y_data   

        if(self.curr_min_x > x_data):
            self.curr_min_x = x_data 

        if(self.curr_min_y > y_data):
            self.curr_min_y = y_data  
        
        self.x_data.append(x_data)
        self.y_data.append(y_data)
        self.running_function.set_xdata(self.x_data)
        self.running_function.set_ydata(self.y_data)
        self.main_plot.set_xlim(self.curr_min_x, self.curr_max_x)
        self.main_plot.set_ylim(self.curr_min_y, self.curr_max_y)
        self.figure.canvas.draw()
        self.figure.canvas.flush_events()
