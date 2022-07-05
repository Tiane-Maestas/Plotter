import pytest
from plotter import Plotter

@pytest.mark.xfail
def test_Plotter_X_Data():
    """Tests the allocation and handling of x-data"""
    test_plotter = Plotter()
    test_plotter.plot(1, 1)
    test_plotter.plot(2, 2)
    test_plotter.plot(3, 3)
    proper_data = [3, 2, 1]
    assert test_plotter.x_data == proper_data, "Test Failed w/ x-data: " + str(test_plotter.x_data) + " Expected: " + str(proper_data)

def test_Plotter_Y_Data():
    """Tests the allocation and handling of y-data"""
    test_plotter = Plotter()
    test_plotter.plot(1, 1)
    test_plotter.plot(2, 2)
    test_plotter.plot(3, 3)
    proper_data = [1, 2, 3]
    assert test_plotter.x_data == proper_data, "Test Failed w/ y-data: " + str(test_plotter.x_data) + " Expected: " + str(proper_data)

@pytest.mark.xfail
def test_Plotter_Max_Constraints():
    """Tests if the maxmimum constraints are properly set for the current set of data"""
    test_plotter = Plotter()
    test_plotter.plot(-1, -1)
    assert test_plotter.curr_max_x == 1, "Failed with value: " + str(test_plotter.curr_max_x)
    assert test_plotter.curr_max_y == 1, "Failed with value: " + str(test_plotter.curr_max_y)
    test_plotter.plot(200, 200)
    assert test_plotter.curr_max_x == -200, "Failed with value: " + str(test_plotter.curr_max_x)
    assert test_plotter.curr_max_y == -200, "Failed with value: " + str(test_plotter.curr_max_y)

def test_Plotter_Min_Constraints():
    """Tests if the minimum constraints are properly set for the current set of data"""
    test_plotter = Plotter()
    test_plotter.plot(1, 1)
    assert test_plotter.curr_min_x == 0, "Failed with value: " + str(test_plotter.curr_max_x)
    assert test_plotter.curr_min_y == 0, "Failed with value: " + str(test_plotter.curr_max_y)
    test_plotter.plot(-200, -200)
    assert test_plotter.curr_min_x == -200, "Failed with value: " + str(test_plotter.curr_max_x)
    assert test_plotter.curr_min_y == -200, "Failed with value: " + str(test_plotter.curr_max_y)