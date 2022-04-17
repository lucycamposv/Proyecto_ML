import pandas as pd
import os
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import pickle


os.chdir(os.path.dirname(__file__))

df = pd.read_csv('data/processed/train_final.csv',index_col=0)
y = pd.read_csv('data/processed/train_target.csv',index_col=0)

#Guardado del modelo
model = Pipeline(steps = [
                ('scaler', StandardScaler()),
                ('model', RandomForestClassifier(n_estimators=100,n_jobs=-1,random_state=42))
])

model.fit(df,y)

with open('new_model','wb') as archivo_salida:
    pickle.dump(model, archivo_salida)