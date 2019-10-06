import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
iris = load_iris()
data1 = pd.DataFrame(data= np.c_[iris['data'], iris['target']],
                     columns= iris['feature_names'] + ['target'])
data1.head()
data1['target']
from sklearn.model_selection import train_test_split
X = data1.iloc[:,0:4]
print(X)
y = data1['target']
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3, random_state=42)
from sklearn import svm
C = 1.0
# SVC with linear kernel
svc = svm.SVC(kernel='linear', C=C).fit(X_train, y_train)
y_pred = svc.predict(X_test)
from sklearn.metrics import confusion_matrix
confusion_matrix(y_test, y_pred)
from sklearn.metrics import accuracy_score
accuracy_score(y_test, y_pred)





