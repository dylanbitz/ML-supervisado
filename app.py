from flask import Flask, render_template

app = Flask(__name__)

@app.route('/regresion-lineal')
def index():
    # toca aprender bootstrap
    link_estilos = "./static/styles.css"
    return render_template(
        "index.html",
        link_estilos,
        presentation="Bienvenidos a mi página web",
        titulo_actividad="WebApp Flask",
    )

if __name__ == '__main__':
    app.run(debug=True)