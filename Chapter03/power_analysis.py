import numpy as np
import matplotlib.pyplot as plt
import statsmodels.stats.power as ssp


stat_power = ssp.TTestPower()
sample_size = stat_power.solve_power(effect_size=0.5, nobs = None, alpha=0.05, power=0.8)
print('Sample Size: {:.2f}'.format(sample_size))

power = stat_power.solve_power(effect_size = 0.5,nobs=33, 
                           alpha = 0.05, power = None)
print('Power = {:.2f}'.format(power))

effect_sizes = np.array([0.2, 0.5, 0.8,1])
sample_sizes = np.array(range(5, 500))
  
stat_power.plot_power(dep_var='nobs', nobs=sample_sizes,
               effect_size=effect_sizes)
plt.xlabel('Sample Size')
plt.ylabel('Power')  
plt.show()