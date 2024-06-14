import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC



class spamDetection:
    def __init__(self):
        self.df=pd.read_csv('Spam Email Detection - spam.csv',encoding='utf-8')
    def naive_bayes(self):
        v1=CountVectorizer()
        l=LabelEncoder()
        x,y=self.df['v2'],l.fit_transform(self.df['v1'])
        x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=42)
        x_train=v1.fit_transform(x_train)
        x_test=v1.transform(x_test)
        model=MultinomialNB()
        model.fit(x_train,y_train)
        predicted=model.predict(x_test)
        return accuracy_score(predicted,y_test)
    
    def logistic_regression(self):
        l=LabelEncoder()
        l1=LabelEncoder()
        x,y=l1.fit_transform(self.df['v2']).reshape(-1,1),l.fit_transform(self.df['v1'])
        x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=42)
        model=LogisticRegression()
        model.fit(x_train,y_train)
        predict=model.predict(x_test)
        return accuracy_score(predict,y_test)

    def svc(self):
        l=LabelEncoder()
        l1=LabelEncoder()
        x,y=l1.fit_transform(self.df['v2']).reshape(-1,1),l.fit_transform(self.df['v1'])
        x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=42)
        model=SVC(kernel='linear')
        model.fit(x_train,y_train)
        predict=model.predict(x_test)
        return accuracy_score(predict,y_test)       

S=spamDetection()

print("Accuracy using Naive Bayes: ",S.naive_bayes())
print("Accuracy using Logistic Regressor: ",S.logistic_regression())
print("Accuracy using Support Vector Classifier: ",S.svc())


