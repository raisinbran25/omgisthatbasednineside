import matplotlib.pyplot as plt
import numpy as np

def plotThis(data):

    # 2. Create the plot
    fig, ax = plt.subplots()
    im = ax.imshow(data, cmap='magma') # 'magma', 'inferno', 'plasma', 'viridis' are great choices


    plt.title("title")
    plt.show()