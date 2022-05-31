# ising_plot.py
# Given a square array of spins, generate a static plot
# Kat Nykiel

# Adapted from https://rajeshrinet.github.io/blog/2014/ising-model/

# TODO: it would be cool to redo this with plotly instead of matplotlib
#       I'll take a look at this when I get back from vacation

# %% codecell
# Import required libraries
import numpy as np
import matplotlib.pyplot as plt

# %% codecell
# Given a square array of spins, generate a static plot
def get_ising_plot(array = [[1/2,-1/2],[-1/2,1/2]]):
    # input: an NxN array corresponding to spins in an Ising model
    # output: a visual representation of the array (matplotlib figure)

    # Verify input is a square numpy array
    ising_array = np.array(array)
    if ising_array.shape[0] != ising_array.shape[1]:
        print("Currently this code only supports square arrays, sorry!")
        return

    # Create the figure
    f = plt.figure()
    nx = range(ising_array.shape[0])
    ny = range(ising_array.shape[1])
    X, Y = np.meshgrid(nx,ny)
    plt.pcolormesh(X, Y, ising_array, cmap=plt.cm.Greys);

    # Format the figure
    frame = plt.gca()
    frame.set_aspect('equal')
    frame.axes.xaxis.set_visible(False)
    frame.axes.yaxis.set_visible(False)
    f.set_dpi(180)

    plt.show()

    return f

# Generate an NxN array of randomly assigned spins (+1/2, -1/2)
N = 256
test_array = (2*np.random.randint(2, size=(N,N))-1)/2
get_ising_plot(test_array)
