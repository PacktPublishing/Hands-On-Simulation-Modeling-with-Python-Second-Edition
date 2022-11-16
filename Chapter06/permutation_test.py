from sklearn.datasets import load_iris
import numpy as np
from sklearn import tree
from sklearn.model_selection import permutation_test_score
import matplotlib.pyplot as plt
import seaborn as sns

data=data = load_iris()
X = data.data
y = data.target

np.random.seed(0)
X_nc_data = np.random.normal(size=(len(X), 4))



clf = tree.DecisionTreeClassifier(random_state=1)

p_test_iris = permutation_test_score(
    clf, X, y, scoring="accuracy", n_permutations=1000
)

print(f"Score of iris flower classification = {p_test_iris[0]}")
print(f"P_value of permutation test for iris dataset = {p_test_iris[2]}")

p_test_nc_data = permutation_test_score(
    clf, X_nc_data, y, scoring="accuracy", n_permutations=1000
)

print(f"Score of no-correletd data classification = {p_test_nc_data[0]}")
print(f"P_value of permutation test for no-correletd dataset = {p_test_nc_data[2]}")

pbox1=sns.histplot(data=p_test_iris[1], kde=True)
plt.axvline(p_test_iris[0],linestyle="-", color='r')
plt.axvline(p_test_iris[2],linestyle="--", color='b')
pbox1.set(xlim=(0,1))
plt.show()

pbox2=sns.histplot(data=p_test_nc_data[1], kde=True)
plt.axvline(p_test_nc_data[0], color="r",linestyle="-")
plt.axvline(p_test_nc_data[2], color="b",linestyle="--")
pbox2.set(xlim=(0,1))
plt.show()