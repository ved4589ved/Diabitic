import pandas as pd
import numpy as np
df = pd.read_csv('diabitic.csv')
X=df.drop(["Diabetes_binary", 'CholCheck', 'Stroke', 'HeartDiseaseorAttack', 'Fruits', 'Veggies', 'AnyHealthcare', 'NoDocbcCost','GenHlth', 'Education', 'Income' ],axis=1)
y=df["Diabetes_binary"]
from sklearn.model_selection import train_test_split
X_train, X_test, y_train,y_test = train_test_split(X,y,test_size = 0.2,random_state = 51)
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=3)
# Train the model using the training sets
knn.fit(X_train,y_train)

def prediction(x):
    x_t=  scaler.transform([x])
    c= knn.predict(x_t)[0]
    if c==1:
        return(True)
    elif c==0:
        return(False)
def prob_dia(x):
    if prediction(x) == True:
        x_t=  scaler.transform([x])
        prec= (knn.predict_proba(x_t)[0][1])*100*0.78
        return('you are diabatic with '+ str(prec)+ ' of probabbility')
    elif prediction(x)== False:
        x_t= scaler.transform([x])
        prec2=(knn.predict_proba(x_t)[0][0])*100*0.78
        return('you are not diabatic with ' + str(prec2)+ ' '+ 'of probabbility')




                    


