import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    "velocidad_kmh": [98, 20, 23, 58, 93, 37, 89, 29, 73, 113,
                      21, 87, 36, 97, 64, 47, 88, 109, 85, 39,
                      117, 68, 86, 103, 70, 46, 116, 79, 31, 44,
                      114, 24, 83, 61, 38, 92, 95, 41, 66, 27,
                      120, 50, 78, 26, 42, 84, 100, 60, 72, 30],
    
    "peso_kg": [1440, 1584, 1345, 887, 1455, 543, 1750, 321, 999, 1866,
                1300, 1905, 1710, 1355, 690, 1333, 1800, 1560, 1400, 620,
                1922, 1550, 1630, 1744, 810, 1480, 1655, 1200, 750, 1380,
                1775, 1990, 890, 1540, 470, 1600, 1325, 910, 1495, 340,
                2000, 720, 1250, 580, 840, 1350, 1705, 1050, 1420, 430],
    
    "consumo_l_100km": [6.63, 9.65, 9.08, 5.75, 6.42, 7.53, 6.80, 8.44, 5.60, 8.53,
                        9.12, 6.89, 7.80, 6.50, 5.90, 7.40, 6.97, 8.02, 5.41, 7.22,
                        8.60, 5.73, 5.48, 7.10, 5.50, 7.00, 8.45, 5.10, 8.20, 6.80,
                        8.75, 9.05, 5.20, 6.05, 7.35, 6.30, 6.55, 7.10, 6.00, 8.55,
                        9.20, 6.40, 5.15, 8.10, 6.70, 5.30, 6.85, 5.80, 5.45, 8.30]
}

df = pd.DataFrame(data)

# Variables independientes y dependiente
x = df[["velocidad_kmh", "peso_kg"]]
y = df["consumo_l_100km"]

# Entrenamiento del modelo
modelo = LinearRegression()
modelo.fit(x, y)

def prediccion(velocidad=0., peso=0.) -> float:
    ''' Esta funcion es la encargada de realizar la predicción de los datos ingresados por el usuario'''
    datos = pd.DataFrame([[velocidad,peso]], columns=["velocidad_kmh", "peso_kg"]) #como el modelo fue entrenado con valores etiquetados, también espera lo mismo al momento de predecir
    prediccion = modelo.predict(datos)
    print(f"Consumo estimado para un vehículo que viaja a {velocidad} km/h y pesa {peso} kg: {prediccion[0]:.2f} L/100km")
    return prediccion
