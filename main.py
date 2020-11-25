import numpy as numpy
import pandas as pd
from sklearn.datasets import *
from sklearn import tree
from dtreeviz.trees import *
import graphviz


df=pd.read_csv('AusOpen-men-2013.csv')
y_name = "Result"
X_name = ["FSP.1","ACE.1","UFE.1"]
X_train = df[X_name]
y_train = df[y_name]
dtree = tree.DecisionTreeClassifier(max_depth=2)
dtree.fit(X_train, y_train)
viz = dtreeviz(dtree,X_train,y_train,
               target_name='Result',
               feature_names=X_name,
               class_names=["Lose","Won"],
               )
 
viz

"""
ターミナルでDesktop/data/に移動
jupyter notebook を打つとブラウザが開いて起動される。
そこから