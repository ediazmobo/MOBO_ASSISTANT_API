from flask import Flask, jsonify, request
import Controller.C_Mobonet as C_Mobonet
from dotenv import load_dotenv
import os

app= Flask(__name__)
# priemr endpoint a si se declara el edpoint o ruta y su proeceso en la funcion predeterminada
@app.route('/')
def root():
    return "Root"

# CREAMOS UNA API DE EJEMPLO metodo GET
@app.route('/users/<user_id>')
def get_user(user_id):
    # lista de ejemplo
    user = {"id": user_id, "name": "Ezequiel", "email": "ediaz@mobo.com.mx"}
    # si queremos obtener algun otro argumento mandado por get simpre y cuando se pase de la manera siguiente /users/15360?query=buscaData
    query = request.args.get('query')
    if query:
        user["query"] = query
    return jsonify(user), 200

#Ahora un ejemplo post
@app.route('/users', methods=['POST'])
def create_user():
    # esto es para obtener la data de nuestro body que pasamos en la peticion
    data = request.get_json()
    # 201 informacion guardada
    data['status'] = 201
    return jsonify(data), 201

# traemos el usuario dependiendo el codigo de empleado de mobonet
@app.route('/dataEmpleado', methods=['POST'])
def consultaUsuario():
    # obtenemos el X-Api-Key y validamos que sea el correcto
    api_key = request.headers.get('X-Api-Key')
    if api_key and api_key == os.getenv('X-API-KEY'):
        # cachamos toda la data que viene del body de la api
        data = request.get_json()
        # obtenemos parametros del body obtenido
        codigoEmpleado = data.get('CodigoEmpleado')
        # mandamos el parametro al controlador
        buscaEmpleado = C_Mobonet.buscaEmpleado(codigoEmpleado)
        buscaEmpleado['code'] = 200
        return jsonify(buscaEmpleado), 200
    else:
        return jsonify({'code': 400, 'error': 'Falta el encabezado X-Api-Key'}), 400
    
# Creamos la ruta de inicio de sesionque viene de mobonet
@app.route('/login', methods=['POST'])
def loginMobonet():
    # obtenemos el X-Api-Key y validamos que sea el correcto
    api_key = request.headers.get('X-Api-Key')
    if api_key and api_key == os.getenv('X-API-KEY'):
        # cachamos toda la data que viene del body de la api
        data = request.get_json()
        # obtenemos parametros del body obtenido
        Usuario = data.get('Usuario')
        Password = data.get('Password')
        data = {
            'usuario': Usuario,
            'password': Password
        }
        # Instanciar la clase C_Mobonet y llamar al método loginMobonet
        controller = C_Mobonet.C_Mobonet()
        # mandamos al controlador de C_Mobonet
        CreaLogin = controller.loginMobonet(data)
        CreaLogin['code'] = 200
        return jsonify(CreaLogin), 200
    else:
        return jsonify({'code': 400, 'error': 'Falta el encabezado X-Api-Key'}), 400
    
    
# Metodos para API
# GET -> OBTENER DATA
# POST -> CREAR DATA
# PUT -> ACTUALIZAR DATA
# DELETE -> ELIMINAR DATA

# inicializamos nuetsro proyecto por ahora que no esta en produccion, en el host local pero en el puerto 800
if __name__ == '__main__':
    app.run(host="127.0.0.1", port="800", debug=True)