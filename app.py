from flask import Flask, render_template, url_for, request
import DecisionTree
import RegresionLineal
import RegresionLogistica
import DecisionTree

app = Flask(__name__)

@app.get('/')
def index():
    link_estilos = "../static/css/index.css"
    return render_template(
        "index.html",
        link=link_estilos,
        titulo="ML Supervisado",
        
    )

@app.get('/caso1-indmusical')
def caso1():
    link_estilos = "../static/css/caso1-.css"
    return render_template(
        "caso1-indmusical.html",
        link=link_estilos,
        titulo="Caso 1 Industria Musical"
        
    )

@app.get('/caso2-IndTexti')
def caso2():
    link_estilos = "../static/css/caso2-.css" 
    return render_template(
        "caso2-.html",
        link=link_estilos,
        
    )

@app.get('/caso3-indFinci')
def caso3():
    link_estilos = "../static/css/caso3-.css" 
    return render_template(
        "caso3-.html",
        link=link_estilos,
        
    )

@app.get('/caso4-indAutomotriz')
def caso4():
    link_estilos = "../static/css/caso4-.css" 
    return render_template(
        "caso4-.html",
        link=link_estilos,
        
    )

@app.get('/regresion-lineal-conceptBasic')
def conceptoBasico():
    link_estilos = "../static/css/conceptBasic.css"
    return render_template(
        "conceptBasic-lin.html",
        link=link_estilos,
        
    )

@app.route('/regresion-lineal-ejercicio', methods=['GET', 'POST'])
def ejercicioPractico():
    link_estilos = "../static/css/ejercicio.css"
    prediccion = 0
    velocidad = None
    peso = None
    if request.method == 'POST':
        velocidad = float(request.form["velocidad"])
        peso = float(request.form["peso"])
        prediccion = RegresionLineal.prediccion(velocidad, peso)
    return render_template(
        "ejercicio-lin.html",
        link=link_estilos,
        grafico=RegresionLineal.graficaModelo(),
        velocidad=velocidad,
        peso=peso,
        resultado=round(prediccion, 2),
    )

@app.get('/regresion-logistica-conceptBasic')
def conceptoBasico_logistica():
    link_estilos = "../static/css/conceptBasic.css"
    return render_template(
        "conceptBasic-log.html",
        link=link_estilos,
        
    )

@app.route('/regresion-logistica-ejercicio', methods=['GET', 'POST'])
def ejercicioPractico_logistica():
    link_estilos = "../static/css/ejerRL.css"
    accuracy, report, _ = RegresionLogistica.evaluate()
    resul = 0
    probabilidad = 0
    if request.method == 'POST':
        values = []
        for res in request.form.values():
            values.append(res)
        _, probabilidad, resul = RegresionLogistica.predict_label(*values)
    return render_template(
        "ejercicio-log.html",
        link=link_estilos,
        exactitud=accuracy,
        reporte=report,
        proba=probabilidad*100,
        resultado=resul,
    )
# ****************Decision Tree*******************
@app.get('/decision-tree/conceptBasic')
def conceptoBasico_decTree():
    link_estilos = "../static/css/conceptBasic.css"
    return render_template(
        "conceptBasic-decTree.html",
        link=link_estilos,
        
    )

app.route('/decision-tree/ejercicio', methods=['GET', 'POST'])
def ejercicioPractico_decTree():
    link_estilos = "../static/css/ejercicio-decTree.css"
    accuracy, report, _ = DecisionTree.evaluate()
    resul = 0
    probabilidad = 0
    if request.method == 'POST':
        features = request.form.to_dict()
        _, probabilidad, resul = DecisionTree.predict_label(features)
>>>>>>> c3ac480a38c680c83f3974fc09704e4f8ec8a806
    return render_template(
        "ejercicio-decTree.html",
        link=link_estilos,
        exactitud=accuracy,
<<<<<<< HEAD
        reporte=report
=======
        reporte=report,
        proba=probabilidad*100,
        resultado=resul,
>>>>>>> c3ac480a38c680c83f3974fc09704e4f8ec8a806
    )

if __name__ == '__main__':
    app.run(debug=True)