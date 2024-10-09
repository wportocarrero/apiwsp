from flask import Flask, request
from datetime import datetime
import time
import pywhatkit

app = Flask(__name__)

@app.route("/enviar-mensaje/<string:celular>/<string:mensaje>", methods=["GET"])
def enviar_mensaje(celular, mensaje):
    try:
        seconds = time.time() + 60
        date = datetime.fromtimestamp(seconds)
        pywhatkit.sendwhatmsg(celular, mensaje, date.hour, date.minute)  # Ajusta la hora y minuto según tus necesidades
        time.sleep(5)
        pywhatkit.sendwhats_image(celular, "fotos.png")
        return {"mensaje": "Mensaje enviado exitosamente"}
    except Exception as e:
        return {"mensaje": "Error al enviar mensaje: " + str(e)}

if __name__ == "__main__":
    app.run(debug=True)