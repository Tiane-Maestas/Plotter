from plotter import Plotter
import numpy

v_0 = 68.355429
deg_0_x = 0.14629
deg_0_y = 0.9892

def func_y(t):
    return -9.8*t**2+v_0*deg_0_y*t

def func_x(t):
    return v_0*deg_0_x*t

def main():
    """Main"""
    plotter1 = Plotter()
    plotter2 = Plotter()
    plotter3 = Plotter()
    plotter4 = Plotter()

    input("Start")
    
    for t in numpy.arange(0, 6.9, 0.1):
        plotter1.plot(func_x(t), func_y(t))
        plotter2.plot(t, t)

    for t in numpy.arange(0, 20, 0.1):
        plotter3.plot(t + 69, t)

    for t in numpy.arange(0, 20, 0.1):
        plotter4.plot(t, -t)
    
    input("End")
    

if __name__ == '__main__':
    main()