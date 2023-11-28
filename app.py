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
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')
