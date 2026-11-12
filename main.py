
# importing libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn
import warnings
warnings.filterwarnings("ignore")
import pickle

df = pd.read_csv("Student_Performance.csv")

# data understanding and exploring
print("------1st 5 rows------------")
print()
print(df.head())

print("------shape of dataset----------")
print()
print(df.shape)

print("------sum of null values----------")
print()
print(df.isnull().sum())

print("------data types----------")
print()
print(df.dtypes)


# visualization

#barchart

plt.bar(df['Hours Studied'], df['Performance Index'])

plt.xlabel('Hours Studied')
plt.ylabel('Performance Index')
plt.title('Hours Studied vs Performance Index')

plt.show()

#histogram
plt.figure(figsize=(7, 4))
plt.hist( df['Performance Index'], color='green', edgecolor='black')
plt.title("Distribution of Student Performance")
plt.xlabel("Performance Index")
plt.ylabel("Number of Students")

plt.show()

# Pie Chart
plt.figure(figsize=(7, 7))

plt.pie(df['Performance Index'].value_counts().head(10), labels=df['Performance Index'].value_counts().head(10).index, autopct='%1.1f%%',startangle=90)
plt.title("Performance Index - Pie Chart")
plt.show()

# Pie Chart
plt.figure(figsize=(7, 7))

plt.pie(
    df['Extracurricular Activities'].value_counts().head(10),
    labels=df['Extracurricular Activities'].value_counts().head(10).index,
    autopct='%1.1f%%',
    startangle=90
)

plt.title("Extracurricular Activities - Pie Chart")
plt.show()


# Data Preprocessing
df['Extracurricular Activities'] = df[
    'Extracurricular Activities'
].map({'Yes': 1, 'No': 0}).astype(int)

X = df.iloc[:, :-1]
y = df.iloc[:, -1]

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0
)

print('-------------train data-------------')
print()
print(X_train.shape)
print(y_train.shape)

print('-------------test data-------------')
print()
print(X_test.shape)
print(y_test.shape)


# model building

from sklearn.linear_model import LinearRegression

obj = LinearRegression()
obj.fit(X_train, y_train)

test_pred = obj.predict(X_test)

# Restrict all predictions between 0 and 100
test_pred = np.clip(test_pred, 0, 100)


# model evaluation

from sklearn.metrics import r2_score, mean_squared_error, root_mean_squared_error


print(f"Test R2score / Accuracy : {r2_score(y_test, test_pred)}")
print(f"Accuracy : {r2_score(y_test, test_pred) * 100}")

print()
print(f"Mean squared error / Loss : {mean_squared_error(y_test, test_pred)}")

print()

print(f"Root Mean squared error : {root_mean_squared_error(y_test, test_pred)}")

print()


# sample prediction testing

print("--------------model verification------------")

sample = [6, 66, 1, 4, 1]

res = obj.predict([sample])

# Restrict sample prediction between 0 and 100
res = np.clip(res, 0, 100)

print()
print(f"Model prediction : {res}")


# saving model

with open('model.pkl', 'wb') as f:
    pickle.dump(obj, f)
