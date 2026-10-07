# import a immportant librarys
from sklearn import linear_model
from sklearn.metrics import r2_score
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd

# read Data
df = pd.read_csv("student_score_prediction_1000.csv")
df = df.fillna(None)

# set x and y
x = df.drop(columns=["id","final_score"])
X = pd.get_dummies(x, drop_first=True)
Y = df["final_score"]

# train and test split
train_x, test_x, train_y, test_y = train_test_split(X, Y, test_size=0.25, random_state=42)


# create a model with polynomial
poly = preprocessing.PolynomialFeatures(degree=2)
poly_train_x = poly.fit_transform(train_x)
poly_test_x = poly.fit_transform(test_x)
# create and fit a model
model = linear_model.LinearRegression()
model.fit(poly_train_x, train_y)
# test model with test_x data
yhat = model.predict(poly_test_x)
train_pred = model.predict(poly_train_x)
test_pred = model.predict(poly_test_x)
# show model score with R2score
print("with degree 2")
print("R2Score = ",r2_score(test_y, yhat))
print("Train R2:", r2_score(train_y, train_pred))
print("Test R2:", r2_score(test_y, test_pred))

age = int(input("Enter age:"))
study_hours = float(input("Enter study_hours:"))
attendance = float(input("Enter attendance:"))
previous_score = float(input("Enter previous_score:"))
sleep_hours = float(input("Enter sleep_hours:"))
homework_hours = float(input("Enter homework_hours:"))
extracurricular = input("Enter extracurricular:")
parent_education = input("Enter parent_education:")
internet_access = input("Enter internet_access:")

new_dataFrame = pd.DataFrame([{
    "age":age,
    "study_hours":study_hours,
    "attendance":attendance,
    "previous_score":previous_score,
    "sleep_hours":sleep_hours,
    "homework_hours":homework_hours,
    "extracurricular":extracurricular,
    "parent_education":parent_education,
    "internet_access":internet_access 
}])

new_x_data = pd.get_dummies(new_dataFrame, drop_first=True)
new_X_data = new_x_data.reindex(columns=X.columns, fill_value=0)
poly_new_X_data = poly.transform(new_X_data)
predication = model.predict(poly_new_X_data)

print("model answer:",predication)
