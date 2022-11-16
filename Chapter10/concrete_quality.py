import pandas as pd
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
from sklearn.metrics import r2_score

features_names= ['Cement','BFS','FLA','Water','SP','CA','FA','Age','CCS']
concrete_data = pd.read_excel('concrete_data.xlsx', names=features_names)


summary = concrete_data.describe()
print(summary)

sns.set(style="ticks")
sns.boxplot(data = concrete_data)

scaler = MinMaxScaler()
print(scaler.fit(concrete_data))
scaled_data = scaler.fit_transform(concrete_data)
scaled_data = pd.DataFrame(scaled_data, columns=features_names)

summary = scaled_data.describe()
print(summary)

sns.boxplot(data = scaled_data)

input_data = pd.DataFrame(scaled_data.iloc[:,:8])
output_data = pd.DataFrame(scaled_data.iloc[:,8])

inp_train, inp_test, out_train, out_test = train_test_split(input_data,output_data, test_size = 0.30, random_state = 1)
print(inp_train.shape)
print(inp_test.shape)
print(out_train.shape)
print(out_test.shape)


model = Sequential()
model.add(Dense(20, input_dim=8, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(1, activation='linear'))
model.compile(optimizer='adam',loss='mean_squared_error',metrics=['accuracy'])
model.fit(inp_train, out_train, epochs=1000, verbose=1)

model.summary()

output_pred = model.predict(inp_test)

print('Coefficient of determination = ')
print(r2_score(out_test, output_pred))

