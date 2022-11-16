import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

mu = 5
sigma =2

P1 = np.random.normal(mu, sigma, 1000)

mu = 10
sigma =2

P2 = np.random.normal(mu, sigma, 1000)

mu = 15
sigma =2

P3 = np.random.normal(mu, sigma, 1000)

mu = 10
sigma =2

P4 = np.random.normal(mu, sigma, 1000)

mu = 10
sigma =1

P5 = np.random.normal(mu, sigma, 1000)

mu = 10
sigma =0.5

P6 = np.random.normal(mu, sigma, 1000)


Plot1 = sns.histplot(P1,stat="density", kde=True, color="g")
Plot2 = sns.histplot(P2,stat="density", kde=True, color="b")
Plot3 = sns.histplot(P3,stat="density", kde=True, color="y")

plt.figure()
Plot4 = sns.histplot(P4,stat="density", kde=True, color="g")
Plot5 = sns.histplot(P5,stat="density", kde=True, color="b")
Plot6 = sns.histplot(P6,stat="density", kde=True, color="y")
plt.show()

