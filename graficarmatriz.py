import sys
# import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

input = np.loadtxt("out_file.txt", dtype='i')
print(input)

plt.imshow(input[::,::],extent=[0,len(input),len(input),0])
plt.grid();

plt.show()