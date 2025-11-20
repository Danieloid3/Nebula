import json


persona = {"nombre": "salva", "edad": 19}

json_texto = json.dumps(persona)

persona_convertida = json.loads(json_texto)

print(persona_convertida["nombre"])

print(persona_convertida["edad"])