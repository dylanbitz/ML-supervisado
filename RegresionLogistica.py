import os
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

datos_diabetes = pd.read_csv('./datasets/diabetes_prediction_dataset.csv') # leemos el dataset

datos_diabetes_procesados = datos_diabetes.copy() # copiamos los resultados para no afectar a la variable con el contenido original
datos_diabetes_procesados = pd.get_dummies(datos_diabetes_procesados) # Tomamos las columnas categoricas y las convertimos en columnas booleanas, para que sean útiles para el modelo

X = datos_diabetes_procesados.drop('diabetes', axis=1) # eliminamos la columna objetivo
y = datos_diabetes_procesados['diabetes'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) # dividimos los datos entre los de entrenamiento y de prueba 80/20

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


model = LogisticRegression()
result = model.fit(X_train, y_train) # entrenamiento del modelo

# buscamos imprimir en consola los resultados brutos, esto no será visto por el usuario final, para esto creamos la función evaluate
prediccion_test = model.predict(X_test)
print(f"La exactitud del modelo es: {accuracy_score(y_test, prediccion_test) * 100:.2f}%")
print(f"Reporte de clasificación:\n {classification_report(y_test, prediccion_test, target_names=['No Diabetes', 'Diabetes'])}")
print(f"Confusion Matrix:\n {confusion_matrix(y_test, prediccion_test)}")

def evaluate():
    '''
    funcion encargada de dar los datos de la evaluación del modelo entrenado, entrega:
    - la exactitud (accuracy)
    - reporte de clasificación
    - matriz de confusión
    '''
    prediccion_test = model.predict(X_test)
    exactitud_modelo = f"La exactitud del modelo es: {accuracy_score(y_test, prediccion_test) * 100:.2f}%"
    reporte = classification_report(y_test, prediccion_test, target_names=['No Diabetes', 'Diabetes'], output_dict=True)
    cm = confusion_matrix(y_test, prediccion_test)
    disp = ConfusionMatrixDisplay(confusion_matrix = cm, display_labels=model.classes_)
    disp.plot(cmap='gray')
    graph_path = os.path.join("static/images", "logistica-matrizConfu.png")
    plt.savefig(graph_path, dpi=60)
    return exactitud_modelo, reporte, cm

def predict_label(age, hypertension, heart_disease, bmi, HbA1c_level, blood_glucose_level, gender, smoking_history, threshold=0.5):
    ''''
    función que se encarga de realizar una predicción sobre diabetes, según los parámetros pedidos
    0 para negativo
    1 para positivo
    '''
    data = {
        'age': age,
        'hypertension': hypertension,
        'heart_disease': heart_disease,
        'bmi': bmi,
        'HbA1c_level': HbA1c_level,
        'blood_glucose_level': blood_glucose_level,
        'gender': gender,
        'smoking_history': smoking_history,
    }
    data = pd.DataFrame([data])
    data = pd.get_dummies(data, columns=['gender', 'smoking_history'])
    
    for col in X.columns:
            if col not in data.columns:
                data[col] = 0
                
    data = data[X.columns]
    data = scaler.transform(data)
    data_scaled = pd.DataFrame(data)
    
    prediccion1 = model.predict(data_scaled)
    prob = model.predict_proba(data_scaled)[0,1]
    prob_legible = f"{prob * 100:.2f}"
    label = "Sí" if prob >= threshold else "No"
    
    return prediccion1[0], prob_legible, label
