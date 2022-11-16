import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.inspection import DecisionBoundaryDisplay

data = pd.read_excel('fault.dataset.xlsx')

print(data.head(10))

print(data.info())

DataStat = data.describe()
print(DataStat)

DataStatCat = data.astype('object').describe()
print(DataStatCat)

fig, axes = plt.subplots(1,2, figsize=(18, 10))
sns.boxplot(ax=axes[0],x='state', y='a1', data=data)
sns.boxplot(ax=axes[1],x='state', y='a2', data=data)
plt.ylim(-40, 40)
plt.show()

X = data.drop('state', axis = 1)
print('X shape = ',X.shape)
Y = data['state']
print('Y shape = ',Y.shape)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.30, random_state = 1)
print('X train shape = ',X_train.shape)
print('X test shape = ', X_test.shape)
print('Y train shape = ', Y_train.shape)
print('Y test shape = ',Y_test.shape)

lr_model = LogisticRegression(random_state=0).fit(X_train, Y_train)
lr_model_score = lr_model.score(X_test, Y_test)
print('Logistic Regression Model Score = ', lr_model_score)

ax1 = DecisionBoundaryDisplay.from_estimator(
    lr_model, X_train, response_method="predict",
     alpha=0.5)
ax1.ax_.scatter(X_train.iloc[:,0], X_train.iloc[:,1], c=Y_train, edgecolor="k")
plt.show()

rm_model = RandomForestClassifier(max_depth=2, random_state=0).fit(X_train, Y_train)
rm_model_score = rm_model.score(X_test, Y_test)
print('Random Forest Model Score = ', rm_model_score)

ax2 = DecisionBoundaryDisplay.from_estimator(
    rm_model, X_train, response_method="predict",
     alpha=0.5)
ax2.ax_.scatter(X_train.iloc[:,0], X_train.iloc[:,1], c=Y_train, edgecolor="k")
plt.show()

mlp_model = MLPClassifier(random_state=1, max_iter=300).fit(X_train, Y_train)
mlp_model_score = mlp_model.score(X_test, Y_test)
print('Artificial Neural Network Model Score = ', mlp_model_score)

ax3 = DecisionBoundaryDisplay.from_estimator(
    mlp_model, X_train, response_method="predict",
     alpha=0.5)
ax3.ax_.scatter(X_train.iloc[:,0], X_train.iloc[:,1], c=Y_train, edgecolor="k")
plt.show()

kn_model= KNeighborsClassifier(n_neighbors=2).fit(X_train, Y_train)
kn_model_score = kn_model.score(X_test, Y_test)
print('K-nearest neighbors Model score =', kn_model_score)

ax4 = DecisionBoundaryDisplay.from_estimator(
    kn_model, X_train, response_method="predict",
     alpha=0.5)
ax4.ax_.scatter(X_train.iloc[:,0], X_train.iloc[:,1], c=Y_train, edgecolor="k")
plt.show()



