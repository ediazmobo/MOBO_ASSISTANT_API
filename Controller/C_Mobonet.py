import Models.M_Mobonet as M_Mobonet
from dotenv import load_dotenv
import os
import requests
import json

class C_Mobonet:
    def __init__(self):
        self.ApiUserMobonet = os.getenv('R_LOGIN_USUARIO')
    def buscaEmpleado(self, codigoEmpleado):
        # MANDAMOS A LLAMARA L MODELO PARA SEGUIR LA ESTRUCTURA MANOLIN
        buscaEmpleado = M_Mobonet.buscaEmpleadoPorCodigo(codigoEmpleado)
        # iteramos y creamos una lista para retornar
        return buscaEmpleado
    def loginMobonet(self, data):
        # Hacer la solicitud POST
        response = requests.post(self.ApiUserMobonet, headers={'Content-Type': 'application/json'}, data=json.dumps(data))
        # Verificar el estado de la respuesta
        if response.status_code == 200:
            # Imprimir la respuesta en formato JSON
            return response.json()
        else:
            # Imprimir el error
            return f"Error {response.status_code}: {response.text}"
        
        
        