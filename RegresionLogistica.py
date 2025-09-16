import os
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report, ConfusionMatrixDisplay
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

datos_diabetes = pd.read_csv('diabetes_prediction_dataset.csv') # leemos el dataset

datos_diabetes_procesados = datos_diabetes.copy() # copiamos los resultados para no afectar a la variable con el contenido original
datos_diabetes_procesados = pd.get_dummies(datos_diabetes_procesados) # Tomamos las columnas categoricas y las convertimos en columnas booleanas, para que sean útiles para el modelo


scaler = MinMaxScaler() # Utilizamos MinMaxScaler para escalar los datos en el rango de 0 a 1
datos_diabetes_procesados_scaled = scaler.fit_transform(datos_diabetes_procesados) # escala los valores de las tablas de 0 a 1
datos_diabetes_procesados_scaled = pd.DataFrame(datos_diabetes_procesados_scaled) # el scaler es un array, acá lo convertimos en un dataframe
datos_diabetes_procesados_scaled.columns = datos_diabetes_procesados.columns # acá recuperamos los nombres de las columnas

X = datos_diabetes_procesados_scaled.drop('diabetes', axis=1) # eliminamos la columna objetivo
y = datos_diabetes_procesados_scaled['diabetes'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) # dividimos los datos entre los de entrenamiento y de prueba 80/20

model = LogisticRegression()
result = model.fit(X_train, y_train) # entrenamiento del modelo

prediccion_test = model.predict(X_test)
print(f"La exactitud del modelo es: {accuracy_score(y_test, prediccion_test) * 100:.2f}%") 