import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


x = np.linspace(0, 1, 100)
y = x + (np.random.rand(len(x)))

for i in range(30):
    x=np.append(x, np.random.choice(x))
    y=np.append(y, np.random.choice(y))

x=x.reshape(-1, 1)
y=y.reshape(-1, 1)

reg_model = LinearRegression().fit(x, y)

r_sq = reg_model.score(x, y)
print(f"R squared = {r_sq}")

alpha=float(reg_model.coef_[0])
print(f"slope: {reg_model.coef_}")
beta=float(reg_model.intercept_[0])
print(f"intercept: {reg_model.intercept_}")

y_pred = reg_model.predict(x)

plt.scatter(x, y)
plt.plot(x, y_pred, linewidth=2)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

boot_slopes = []
boot_interc = []
r_sqs= []
n_boots = 500
num_sample = len(x)
data = pd.DataFrame({'x': x[:,0],'y': y[:,0]})

plt.figure()
for k in range(n_boots):
 sample = data.sample(n=num_sample, replace=True)
 x_temp=sample['x'].values.reshape(-1, 1)
 y_temp=sample['y'].values.reshape(-1, 1)
 reg_model = LinearRegression().fit(x_temp, y_temp)
 r_sqs_temp = reg_model.score(x_temp, y_temp)
 r_sqs.append(r_sqs_temp)
 boot_interc.append(float(reg_model.intercept_[0]))
 boot_slopes.append(float(reg_model.coef_[0]))
 y_pred_temp = reg_model.predict(x_temp)
 plt.plot(x_temp, y_pred_temp, color='grey', alpha=0.2)

plt.scatter(x, y)
plt.plot(x, y_pred, linewidth=2)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

sns.histplot(data=boot_slopes, kde=True)
plt.show()
sns.histplot(data=boot_interc, kde=True)
plt.show()

plt.plot(r_sqs)

max_r_sq=max(r_sqs)
print(f"Max R squared = {max_r_sq}")

pos_max_r_sq=r_sqs.index(max(r_sqs))
print(f"Boot of the best Regression model = {pos_max_r_sq}")

max_slope=boot_slopes[pos_max_r_sq]
print(f"Slope of the best Regression model = {max_slope}")

max_interc=boot_interc[pos_max_r_sq]
print(f"Intercept of the best Regression model = {max_interc}")