import numpy as np
import matplotlib.pyplot as plt


def maxwell_boltzmann(c, m, t):
    '''
        This is a function that computes the Maxwell-Boltzmann Distribution for:
            - `c`: np.array of speeds
            - `m`: mass of the gas of interest
            - `t`: temperature of the system of interest
    '''
    k = 8.31446261815324 # J / (mol * K)
    return(4.*np.pi * ((m / (2 * np.pi * k * t))**1.5) * (c**2) * np.exp(- (m * c**2)/(2 * k * t)))

colors = ['dodgerblue', 'tab:orange', 'crimson', 'tab:purple', 'mediumspringgreen', 'fuchsia']
plt.figure(figsize=(12, 8), dpi=150)
speeds = np.linspace(0, 4000, 1000)
temperature_values = [150, 200, 250, 300,400]

for ii in range(len(temperature_values)):
    plt.plot(speeds, maxwell_boltzmann(speeds, 2.016/1000, temperature_values[ii]), color=colors[ii], label=r'$'+str(temperature_values[ii])+'$')

plt.xlim(0, 4000)
plt.xlabel(r'$c$')
plt.ylabel(r'$f(c)$')
plt.title('Maxwell-Boltzmann Distribution of H$_2$ at Various Temperatures')
legend = plt.legend(title='T (Kelvin)', ncol=1, fontsize=10)
plt.annotate(r'$f(c) = 4 \pi\  c^{2} \left( \frac{m}{2 \pi KT} \right)^{\frac{3}{2}}\  \exp{\left( - \frac{m c^{2}}{2 K T} \right)}$',
             xy=(0.455, 0.75), xycoords='figure fraction', fontsize=12)

#plt.savefig('Maxwell-Boltzmann-Distribution_Temperature-Dependence-H2.pdf', dpi=300)

plt.show()