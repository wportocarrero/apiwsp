FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expone el puerto que Render utiliza
EXPOSE 10000

CMD ["python3", "envio.py"]  # Cambia "app.py" al nombre de tu archivo principal