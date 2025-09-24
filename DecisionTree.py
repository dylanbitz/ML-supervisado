import os
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
    'Inflation rate',
    'Course'
], axis=1)
X = datos_estudiantes_process.drop("Output", axis=1)
y = datos_estudiantes_process['Output']

colums_catg = ["Application mode", "Marital status",
                    "Mother's occupation", "Father's occupation"]

preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), colums_catg)
    ],
    remainder="passthrough"  # deja las demás columnas como están
)
model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("classifier", DecisionTreeClassifier(max_depth=12,random_state=0))
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

def predict_label(features:dict):
    ''''
    Realiza una predicción sobre el estado del estudiante usando los features de X.columns.
    Los argumentos deben coincidir con los nombres de las columnas de X.
    '''
    data = {col: features.get(col, 0) for col in X.columns}
    df = pd.DataFrame([data])
    
    for col in X.columns:
            if col not in df.columns:
                data[col] = 0

    pred = model.predict(df)
    prob = model.predict_proba(df)[0,1]
    label_map = {0: "Deserción", 1: "Seguirá cursando", 2: "Graduado"}
    label = label_map.get(int(pred[0]), "Desconocido")
    
    return pred[0], prob, label