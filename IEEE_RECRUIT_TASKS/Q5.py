#MatPlotLib(Normal/Gaussian distribution)

import numpy as np
import matplotlib.pyplot as plt

randoms=np.random.normal(0,1,1000) #creates a normal distribution where mean=0,std.dev=1,size=1000 

plt.scatter(range(len(randoms)),randoms,alpha=0.5)#alpha controls the transparency of points

plt.xlabel("sample index")
plt.ylabel("Random Values")
plt.title("Scatter graph of 1000 random numbers (normal distribution)")

plt.show()

#here the mean and std.dev wont be exactly 0 and 1 but if I increase sample size they will 
# come near to specified values earlier
print("mean",np.mean(randoms)) 
print("std deviation",np.std(randoms))
