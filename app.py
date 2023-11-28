from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

# Lista de preguntas de la encuesta
preguntas_encuesta = [
    "¿Cómo calificarías nuestro servicio?",
    "¿Cuál es tu característica favorita de nuestro producto?",
    "¿Qué mejorarías en nuestra empresa?",
]

# Almacenar respuestas de la encuesta
respuestas_encuesta = {pregunta: [] for pregunta in preguntas_encuesta}

@app.route('/')
def index():
    return render_template('templates/index.html', preguntas=preguntas_encuesta)

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
    # Obtener el puerto de OpenShift si está disponible, de lo contrario, usar 8080
    port = int(os.environ.get('PORT', 8080))
    
    # Configuración para permitir conexiones desde cualquier origen
    app.config['CORS_HEADERS'] = 'Content-Type'
    
    # Ejecutar la aplicación
    app.run(port=port, host='0.0.0.0', debug=True)
