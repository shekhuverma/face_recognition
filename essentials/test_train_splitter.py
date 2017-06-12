# Importing the libraries
import numpy as np
import os
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('data.csv')
X = dataset.iloc[:,0].values

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test = train_test_split(X,test_size = 0.3,random_state = 0)
X_test.astype(str).reshape(X_test.size,1)
for a in X_test:
    final=os.path.join("testdata",a)
    os.rename(a,final)