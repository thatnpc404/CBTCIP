from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import pandas as pd


class Classification:
    def __init__(self):
        self.df=pd.read_csv('Iris Flower - Iris.csv',encoding='utf-8')
        self.x=self.df[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
        self.y=self.df['Species']
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(self.x, self.y, test_size=0.4, random_state=42)

    def randomForestClassifier(self):
        model=RandomForestClassifier()
        fit_=model.fit(self.x_train,self.y_train)
        predicted=fit_.predict(self.x_test)
        print(accuracy_score(self.y_test,predicted))
    
    def decisionTreeClassifier(self):
        model=DecisionTreeClassifier(max_depth=4)
        fit_=model.fit(self.x_train,self.y_train)
        predicted=fit_.predict(self.x_test)
        print(accuracy_score(self.y_test,predicted))

    def supportVectorClassifier(self):
        model=SVC()
        fit_=model.fit(self.x_train,self.y_train)
        predicted=fit_.predict(self.x_test)
        print(accuracy_score(self.y_test,predicted))
    

C=Classification()
print('Random Forest Classifier')
C.randomForestClassifier()
print('Decision Tree Classifier')
C.decisionTreeClassifier()
print('Support Vector Classifier')
C.supportVectorClassifier()
