# import libraries

import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from pickle import *

# load the data
data = pd.read_csv("diabetes23.csv")
print(data)

# handle the data
print(data.isnull().sum())

# features and target
features = data[["FS", "FU"]]
target = data["Diabetes"]

# handle cat data
nfeatures = pd.get_dummies(features)
print(features)
print(nfeatures)

# train and test
x_train, x_test, y_train, y_test = train_test_split(nfeatures, target, random_state=0)

# model
model = RandomForestClassifier(n_estimators=10)
model.fit(x_train, y_train)

# performance
cr = classification_report(y_test, model.predict(x_test))
print(cr)

# model selection
f = None
try:
	f = open("diab.model", "wb")
	dump(model, f)
except Exception as e:
	print("issue ", e)
finally:
	if f is not None:
		f.close()