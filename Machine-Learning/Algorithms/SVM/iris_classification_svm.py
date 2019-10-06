#Import necessary libraries

import pandas as pd # Pandas - Array and data manipulation
import numpy as np # Numpy - For computational purposes

#Sklean has default datasets which can be imported as the below library
from sklearn.datasets import load_iris

#loading iris dataset
iris = load_iris()

#Converting the array into Dataframe for easier manipulation
data1 = pd.DataFrame(data= np.c_[iris['data'], iris['target']],
                     columns= iris['feature_names'] + ['target'])

#To Display the first 5 records of our dataset
data1.head()

#Viewing a single column in the dataset using the column name
data1['target']

#Splitting the dataset into traain and test 
from sklearn.model_selection import train_test_split

#The X contains the features
X = data1.iloc[:,0:4]
print(X)

#The target class is stored in y
y = data1['target']

#Splitting the X and y into Train and test dataset
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3, random_state=42)

#Importing the SVM for classification
from sklearn import svm
C = 1.0

# SVC with linear kernel and training the model usign the training dataset
svc = svm.SVC(kernel='linear', C=C).fit(X_train, y_train)

#Predicting from the X_test-  Test data featues
#the prediction is stored in y_pred
y_pred = svc.predict(X_test)

#To evaluate the mode, the y_pred and y_test is compared and evaluated using Confusion Matrix
from sklearn.metrics import confusion_matrix
confusion_matrix(y_test, y_pred)

#Printing the accuracy Score
from sklearn.metrics import accuracy_score
accuracy_score(y_test, y_pred)





