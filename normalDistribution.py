import numpy as np
import matplotlib.pyplot as plt

def normal_random_numbers(mean,std,size):
    random_array=np.random.normal(mean,std,size)
    return random_array


#Graph for single Sample Size

random_array = normal_random_numbers(0, 1, 500)
frequencies, bins, _ = plt.hist(random_array, bins=20, color='teal', alpha=0.4, edgecolor='teal')
plt.title(f'Histogram for Sample Size: 500')
plt.ylabel('Frequency')
plt.xlabel('Value Range')

## Calculate midpoints of bins
bin_midpoints = 0.5 * (bins[:-1] + bins[1:])

## Smooth the curve using spline interpolation
plt.plot(bin_midpoints, frequencies,color='red', linestyle='-')

plt.show()

import numpy as np
import matplotlib.pyplot as plt

def normal_random_numbers(mean,std,size):
    random_array=np.random.normal(mean,std,size)
    return random_array
#Simulation for different Sample Sizes

sample_sizes=[100,1000,10000,100000]
colors = ['dodgerblue', 'tab:orange', 'lime', 'crimson']

fig, axs = plt.subplots(2,2, figsize=(12, 10),sharex=True)
axs=axs.flatten()

for ii in range(len(sample_sizes)):
    random_array = normal_random_numbers(0, 1, sample_sizes[ii])
    frequencies, bins, _ = axs[ii].hist(random_array, bins=20, color=colors[ii], alpha=0.5, edgecolor='black')
    axs[ii].set_title(f'Histogram for Sample Size: {sample_sizes[ii]}')
    axs[ii].set_ylabel('Frequency')
    axs[ii].set_xlabel('Value Range')
    ## Calculate midpoints of bins
    bin_midpoints = 0.5 * (bins[:-1] + bins[1:])
    ## Smooth the curve using spline interpolation
    axs[ii].plot(bin_midpoints, frequencies,color='red', linestyle='-')

plt.subplots_adjust(hspace=0.4)
plt.show()