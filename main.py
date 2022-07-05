import numpy
from plotter import Plotter

V_0 = 68.355429
DEG_0_X = 0.14629
DEG_0_Y = 0.9892

def func_y(time):
    """Funtion that outputs a parabola"""
    return -9.8*time**2+V_0*DEG_0_Y*time

def func_x(time):
    """Function that outputs a line"""
    return V_0*DEG_0_X*time

def main():
    """Main"""
    plotter_1 = Plotter(title="Plot Uno", xlabel="x-axis1", ylabel="y-axis1", color='g')
    plotter_2 = Plotter(title="Plot Dos", xlabel="X2", ylabel="2y")
    plotter_3 = Plotter(title="Plot 3", xlabel="3x", ylabel="Y3", color='y')
    plotter_4 = Plotter(title="Plot 4", xlabel="4-axe", ylabel="4 Why?", color='r')

    input("Start")
    
    for time in numpy.arange(0, 6.9, 0.1):
        plotter_1.plot(func_x(time), func_y(time))
        plotter_2.plot(time, time)
    
    for time in numpy.arange(0, 20, 0.1):
        plotter_3.plot(time + 69, time)
    
    for time in numpy.arange(0, 20, 0.1):
        plotter_4.plot(time, -time)
    
    input("End")    

if __name__ == '__main__':
    main()
