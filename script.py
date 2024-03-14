from usuario import Usuario
from datetime import datetime
import os
import json
archivo = None
log = None
instancias = []

try:
    with open('usuarios.txt', 'r') as archivo:
        for line in archivo:
            usuario = json.loads(line)
            instancias.append(Usuario(usuario.get('nombre'), usuario.get('apellido'), usuario.get('email'), usuario.get('genero')))

    # for i in range(len(instancias)):
    #     print(f'instancias: {instancias[0].apellido}')
    #     print(f'Nombre: {instancias[i].nombre}, Apellido: {instancias[i].apellido}, Email: {instancias[i].email}, Género: {instancias[i].genero}')

except FileNotFoundError as e:
    print("No se encontró el archivo.", e)
except Exception as e:
    print("Se produjo error JSONDecodeError al leer el archivo.", e)

    fecha_actual = datetime.now()
    with open(f"error.log", "w") as log:
            log.write(f"{fecha_actual} - [ERROR]: {e}\n")

finally:
    if archivo is not None:
        archivo.close()
    elif log is not None:
        log.close()
