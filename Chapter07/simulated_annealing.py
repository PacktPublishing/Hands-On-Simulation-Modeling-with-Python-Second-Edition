import numpy as np
import matplotlib.pyplot as plt

x= np.linspace(0,10,1000)


def cost_function(x):
    return x*np.sin(2.1*x+1)

plt.plot(x,cost_function(x))
plt.xlabel('X')
plt.ylabel('Cost Function')
plt.show()

temp = 2000
iter = 2000
step_size = 0.1
np.random.seed(15)
xi = np.random.uniform(min(x), max(x))
E_xi = cost_function(xi)
xit, E_xit = xi, E_xi
cost_func_eval = []
acc_prob = 1

for i in range(iter):
        xstep = xit + np.random.randn() * step_size  
        E_step = cost_function(xstep)
        if E_step < E_xi:
            xi, E_xi = xstep, E_step
            cost_func_eval.append(E_xi)
            print('Iteration = ',i, 'x_min = ',xi,'Global Minimum =', E_xi,
                                     'Acceptance Probability =', acc_prob)
        diff_energy = E_step - E_xit
        t = temp /(i + 1)
        acc_prob = np.exp(-diff_energy/ t)
        if diff_energy < 0 or np.random.randn() < acc_prob:
            xit, E_xit = xstep, E_step


plt.plot(cost_func_eval, 'bs--')
plt.xlabel('Improvement Step')
plt.ylabel('Cost Function improvement')
plt.show()