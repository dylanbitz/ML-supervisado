from flask import Flask, render_template, url_for, request
import RegresionLineal
import RegresionLogistica

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
        "conceptBasic.html",
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
        "ejercicio.html",
        link=link_estilos,
        grafico=RegresionLineal.graficaModelo(),
        velocidad=velocidad,
        peso=peso,
        resultado=round(prediccion, 2),
    )
@app.get('/regresion-logistica-conceptBasic')
def comBasRL():
    link_estilos = "../static/css/comBasRL.css"
   
    return render_template(
        "comBasRL.html",
        link=link_estilos,
    )


@app.route('/regresion-logistica-ejercicio', methods=['GET', 'POST'])
def ejerRL():
    link_estilos = "../static/css/ejerRL.css"
   

    return render_template(
        "ejerRL.html",
        link=link_estilos,
    )
    
    
    
    
@app.get('/regresion-logistica-conceptBasic')
def conceptoBasico_logistica():
    link_estilos = "../static/css/conceptBasic.css"
    return render_template(
        "conceptBasic-log.html",
        link=link_estilos,
        
    )

if __name__ == '__main__':
    app.run(debug=True)