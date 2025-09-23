import os
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

datos_estudiantes = pd.read_csv('./datasets/student_data.csv', sep=';')
datos_estudiantes.rename(columns={'Nacionality':'Nationality', 'Age at enrollment':'Age'}, inplace=True) # Renombramos algunas columnas para mejor legibilidad
datos_estudiantes_process = datos_estudiantes.copy()
datos_estudiantes_process['Output'] = datos_estudiantes_process['Output'].map({ # acá buscamos asignar valores númericos al target
    'Dropout':0,
    'Enrolled':1,
    'Graduate':2
})

datos_estudiantes_process = datos_estudiantes_process.drop(columns=[
    'Nationality',
    'Mother\'s qualification',
    'Father\'s qualification', 
    'Educational special needs', 
    'International', 
    'Curricular units 1st sem (without evaluations)',
    'Unemployment rate', 
    'Inflation rate'
], axis=1)
X = datos_estudiantes_process.drop("Output", axis=1)
y = datos_estudiantes_process['Output']

colums_catg = ["Course", "Application mode", "Marital status",
                    "Mother's occupation", "Father's occupation"]

preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), colums_catg)
    ],
    remainder="passthrough"  # deja las demás columnas como están
)
model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("classifier", DecisionTreeClassifier(max_depth=15,random_state=0))
])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model.fit(X_train, y_train)

def evaluate():
    '''
    funcion encargada de dar los datos de la evaluación del modelo entrenado, entrega:
    - la exactitud (accuracy)
    - reporte de clasificación
    - matriz de confusión
    '''
    prediccion_test = model.predict(X_test)
    exactitud_modelo = f"La exactitud del modelo es: {accuracy_score(y_test, prediccion_test) * 100:.2f}%"
    reporte = classification_report(y_test, prediccion_test,target_names=['Desercion', 'En curso', 'Graduado'], output_dict=True)
    cm = confusion_matrix(y_test, prediccion_test)
    disp = ConfusionMatrixDisplay(confusion_matrix = cm, display_labels=model.classes_)
    disp.plot(cmap='gray')
    graph_path = os.path.join("static/images", "decTree-matrizConfu.png")
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