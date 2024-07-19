import numpy as np
import matplotlib.pyplot as plt

def uniform_random_numbers(a,b,n):
    random_array=np.random.uniform(a,b,n)
    return random_array

#Graph for one one sample Size

random_array=uniform_random_numbers(0,1,500)
frequencies,bins,_ = plt.hist(random_array, bins=20, range=(0, 1), color='teal', alpha=0.4, edgecolor='black')
plt.title(f'Histogram for Sample Size: 500')
plt.ylabel('Frequency')
plt.xlabel('Value Range')

bin_midpoints = 0.5 * (bins[:-1] + bins[1:])  ## Calculate midpoints of bins

plt.plot(bin_midpoints, frequencies, color='red', linestyle='-') ## Smooth the curve using spline interpolation

plt.show()

def uniform_random_numbers(a,b,n):
    random_array=np.random.uniform(a,b,n)
    return random_array

# Simulation for different Sample Sizes
sample_sizes=[100,1000,10000,100000]
colors = ['dodgerblue', 'tab:orange', 'lime', 'crimson']

fig, axs = plt.subplots(2,2, figsize=(12, 10),sharex=True)

axs=axs.flatten()

for ii in range(len(sample_sizes)):
    random_array=uniform_random_numbers(0,1,sample_sizes[ii])
    frequencies,bins,_ = axs[ii].hist(random_array, bins=20, range=(0, 1), color=colors[ii], alpha=0.4, edgecolor='black')
    axs[ii].set_title(f'Histogram for Sample Size: {sample_sizes[ii]}')
    axs[ii].set_ylabel('Frequency')
    axs[ii].set_xlabel('Value Range')

    bin_midpoints = 0.5 * (bins[:-1] + bins[1:])  ## Calculate midpoints of bins

    axs[ii].plot(bin_midpoints, frequencies, color='red', linestyle='-') ## Smooth the curve using spline interpolation

plt.subplots_adjust(hspace=0.4)
plt.show()