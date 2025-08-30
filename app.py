from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    link_estilos = "./static/styles.css" #tienen que modificar el último nombre styles.css a su propio archivo css
    return render_template(
        "base.html",
        link=link_estilos,
        titulo="ML Supervisado",
        presentation="Bienvenidos a mi página web",
    )

@app.route('/caso1-')
def caso1():
    return render_template(
        "caso1-.html",
    )

if __name__ == '__main__':
    app.run(debug=True)