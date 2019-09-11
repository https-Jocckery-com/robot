import matplotlib.pyplot as plt
import numpy as numpy
with open("detected_data.txt", mode = "r") as file:
    d_data = file.read().split("\n")
with open("gt_data.txt", mode = "r") as file:
    g_data = file.read().split("\n")
plt.plot(d_data, g_data, marker = ".", markersize = 3)
plt.title("data")
plt.xlabel("detected area")
plt.xlabel("ground truth area")
plt.show()