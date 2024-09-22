from flask import Flask, request, jsonify
from flask_cors import CORS
from marshmallow import Schema, fields, ValidationError

app = Flask(__name__)
CORS(app)

class ContactSchema(Schema):
    nombre = fields.Str(required=True)
    apellido = fields.Str(required=True)
    correo = fields.Email(required=True)
    asunto = fields.Str(required=True)
    mensaje = fields.Str(required=True)
    servicio =  fields.Str(required=True)

@app.route("/contacto", methods=["POST"])
def send_contact_form():
    json_data = request.get_json()
    schema = ContactSchema()

    try:
        # Validar los datos
        data = schema.load(json_data)
        # Aquí puedes agregar la lógica para enviar un correo o guardar los datos
        
        return jsonify({"success": "ok"}), 200

    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)
