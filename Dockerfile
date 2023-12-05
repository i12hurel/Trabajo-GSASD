# Usa la imagen base de Python
FROM python:3.8

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia los archivos necesarios al contenedor
COPY requirements.txt .
COPY application.py .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto 8080 (ajusta según la configuración de tu aplicación)
EXPOSE 8080

# Ejecuta la aplicación cuando se inicia el contenedor
CMD ["gunicorn", "application:app", "--bind", "0.0.0.0:8080", "--workers", "4"]
