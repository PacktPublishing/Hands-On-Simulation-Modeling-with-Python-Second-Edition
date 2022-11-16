import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import matplotlib.pyplot as plt
from sklearn.feature_selection import SelectKBest, chi2

data = pd.read_excel('UAV_WiFi.xlsx')

print(data.info())

DataStatCat = data.astype('object').describe()
print(DataStatCat)

X = data.drop('target', axis = 1)
print('X shape = ',X.shape)
Y = data['target']
print('Y shape = ',Y.shape)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.30, random_state = 1)
print('X train shape = ',X_train.shape)
print('X test shape = ', X_test.shape)
print('Y train shape = ', Y_train.shape)
print('Y test shape = ',Y_test.shape)


SVC_model = SVC(gamma='scale',random_state=0).fit(X_train, Y_train)
SVC_model_score = SVC_model.score(X_test, Y_test)
print('Support Vector Classification Model Score = ', SVC_model_score)

first_10_columns = X.iloc[:,0:5]
plt.figure(figsize=(10,5))
first_10_columns.boxplot()

X_scaled = (X-X.min())/(X.max()-X.min())

first_10_columns = X_scaled.iloc[:,0:5]
plt.figure(figsize=(10,5))
first_10_columns.boxplot()

best_input_columns = SelectKBest(chi2, k=10).fit(X_scaled, Y)
sel_index = best_input_columns.get_support()
best_X = X_scaled.loc[: , sel_index]

feature_selected = best_X.columns.values.tolist()
print("The best 10 feature selected are:", feature_selected)

X_train, X_test, Y_train, Y_test = train_test_split(best_X, Y, test_size = 0.30, random_state = 1)
print('X train shape = ',X_train.shape)
print('X test shape = ', X_test.shape)
print('Y train shape = ', Y_train.shape)
print('Y test shape = ',Y_test.shape)

SVC_model = SVC(gamma='auto',random_state=0).fit(X_train, Y_train)
SVC_model_score = SVC_model.score(X_test, Y_test)
print('Support Vector Classification Model Score = ', SVC_model_score)
