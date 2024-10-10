from flask import Flask, jsonify
from twilio.rest import Client
import os
import re

app = Flask(__name__)

# Configuración de Twilio usando variables de entorno
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

def validar_numero(celular):
    # Validar el formato del número de teléfono (simple regex para ejemplo)
    return re.match(r'^\+\d{1,15}$', celular)

@app.route("/enviar-mensaje/<string:celular>/<int:estado>", methods=["GET"])
def enviar_mensaje(celular, estado):
    if not validar_numero(celular):
        return jsonify({"mensaje": "Número de teléfono inválido."}), 400
    
    if estado == 1:
        mensaje = "Puerta abierta."
    elif estado == 0:
        mensaje = "Puerta cerrada."
    else:
        return jsonify({"mensaje": "Estado inválido. Usa 1 o 0."}), 400

    try:
        mensaje_enviado = client.messages.create(
            from_="whatsapp:+14155238886",
            body=mensaje,
            to="whatsapp:" + celular
        )
        return jsonify({"mensaje": "Mensaje enviado exitosamente."}), 200
    except Exception as e:
        return jsonify({"mensaje": "Error al enviar mensaje: " + str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

