from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

# Lista de preguntas de la encuesta
preguntas_encuesta = [
    "¿Cómo te llamas?",
    "¿Cuál es tu color favorito?",
    "¿Cuál es tu asignatura favorita?",
]

# Almacenar respuestas de la encuesta
respuestas_encuesta = {pregunta: [] for pregunta in preguntas_encuesta}

@app.route('/')
def index():
    return render_template('index.html', preguntas=preguntas_encuesta)

@app.route('/submit', methods=['POST'])
def submit():
    for pregunta in preguntas_encuesta:
        respuesta = request.form.get(pregunta)
        respuestas_encuesta[pregunta].append(respuesta)

    return redirect('/gracias')

@app.route('/gracias')
def gracias():
    return "¡Gracias por completar la encuesta!"

if __name__ == '__main__':
    # Usamos gunicorn para el servidor en lugar del servidor de desarrollo de Flask
    from gunicorn.app.base import BaseApplication
    class StandaloneApplication(BaseApplication):
        def __init__(self, app, options=None):
            self.options = options or {}
            self.application = app
            super(StandaloneApplication, self).__init__()

        def load_config(self):
            for key, value in self.options.items():
                self.cfg.set(key, value)

        def load(self):
            return self.application

    options = {
        'bind': '0.0.0.0:8080',
        'workers': 4  # Ajusta el número de workers según tus necesidades
    }

    StandaloneApplication(app, options).run()
