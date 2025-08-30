from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # toca aprender bootstrap
    return render_template(
        "index.html",
        presentation="Bienvenidos a mi página web",
        titulo_actividad="WebApp Flask",
    )

if __name__ == '__main__':
    app.run(debug=True)