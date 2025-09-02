from flask import Flask, render_template

app = Flask(__name__)

@app.get('/')
def index():
    link_estilos = "../static/css/index.css" #tienen que modificar el último nombre styles.css a su propio archivo css
    return render_template(
        "index.html",
        link=link_estilos,
        titulo="ML Supervisado",
        
    )

@app.get('/caso1-indmusical')
def caso1():
    link_estilos = "../static/css/caso1-.css" #tienen que modificar el último nombre styles.css a su propio archivo css
    return render_template(
        "caso1-indmusical.html",
        link=link_estilos,
        titulo="Caso 1 Industria Musical"
        
    )

@app.get('/caso2-')
def caso2():
    link_estilos = "../static/css/caso2-.css" #tienen que modificar el último nombre styles.css a su propio archivo css
    return render_template(
        "caso2-.html",
        link=link_estilos,
        
    )

@app.get('/caso3-')
def caso3():
    link_estilos = "../static/css/caso3-.css" #tienen que modificar el último nombre styles.css a su propio archivo css
    return render_template(
        "caso3-.html",
        link=link_estilos,
        
    )

@app.get('/caso4-')
def caso4():
    link_estilos = "../static/css/caso4-.css" #tienen que modificar el último nombre styles.css a su propio archivo css
    return render_template(
        "caso4-.html",
        link=link_estilos,
        
    )

if __name__ == '__main__':
    app.run(debug=True)