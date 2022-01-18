import pandas as pd
import numpy as np
df = pd.read_csv('diabitis_clean3.csv')
X=df.drop(["Diabetes_binary"],axis=1)
y=df["Diabetes_binary"]
from sklearn.model_selection import train_test_split
X_train, X_test, y_train,y_test = train_test_split(X,y,test_size = 0.2,random_state = 51)
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)
from sklearn.linear_model import LogisticRegression
L_R=LogisticRegression(random_state=0).fit(X_train,y_train)
y_train_pred = L_R.predict(X_train)
y_test_pred = L_R.predict(X_test)
def prediction(x):
    x_t=  scaler.transform([x])
    c= L_R.predict(x_t)[0]
    if c==1:
        return(True)
    elif c==0:
        return(False)

def prob_dia(x):
    if prediction(x) == True:
        x_t=  scaler.transform([x])
        prec= (L_R.predict_proba(x_t)[0][1])*100
        return('you are Diabetes with '+ str(prec)+ '% of probabbility')
    elif prediction(x)== False:
        x_t= scaler.transform([x])
        prec2=(L_R.predict_proba(x_t)[0][0])*100
        return('you are not Diabetes with '+ str(prec2)+ '% of probabbility')




                    


