'''
Takes a positional data set (time, x, y, z) and applies the Savintzky Golay filter on it based on the
polynomial and window parameters we input
'''

from math import *
import numpy as np
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from scipy.signal import savgol_filter
from util import read_data
#import pandas as pd : This is for testing the function
import matplotlib.pyplot as plt


def golay(data, window, degree):
    '''
    Apply the Savintzky-Golay filter to a positional data set.

    Args:
        data (numpy array): containing all of the positional data in the format of (time, x, y, z)
        window (int): window size of the Savintzky-Golay filter
        degree (int): degree of the polynomial in Savintzky-Golay filter

    Returns:
        numpy array: filtered data in the same format
    '''

    x = data[:, 1]
    y = data[:, 2]
    z = data[:, 3]

    x_new = savgol_filter(x, window, degree)
    y_new = savgol_filter(y, window, degree)
    z_new = savgol_filter(z, window, degree)


    new_positions = np.zeros((len(data), 4))
    new_positions[:, 1] = x_new
    new_positions[:, 2] = y_new
    new_positions[:, 3] = z_new
    new_positions[:, 0] = data[:, 0]

    return new_positions



# if __name__ == "__main__":
#     pd.set_option('display.width', 1000)
#     my_data = read_data.load_data('../example_data/orbit.csv')
#     print(len(my_data))
#     window = 21 # its better to select it as the len(data)/3 and it needs to be an odd number
#     degree = 6
#     positions_filtered = golay(my_data, window, degree)
#     #print(positions_filtered - my_data)
#     fig = plt.figure()
#     p = plt.plot(my_data[0:1000,0],my_data[0:1000,1],'-',color = 'red',label="x axis")
#     p = plt.plot(my_data[0:1000,0],my_data[0:1000,2],'-',color = 'blue',label="y axis")
#     p = plt.plot(my_data[0:1000,0],my_data[0:1000,3],'-',color = 'green',label="z axis")
#     p = plt.plot(my_data[0:1000,0],positions_filtered[0:1000,1],color="yellow",label="new_x axis")
#     p = plt.plot(my_data[0:1000,0],positions_filtered[0:1000,2],color="violet",label="new_y axis")
#     p = plt.plot(my_data[0:1000,0],positions_filtered[0:1000,3],color="black",label="new_z axis")
#     plt.legend(loc="lower right")
#     plt.show()
