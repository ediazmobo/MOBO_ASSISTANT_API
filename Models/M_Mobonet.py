from App.dataBase import ConexionMobonet

def buscaEmpleadoPorCodigo(codigoEmpleado):
    conn = ConexionMobonet()
    try:
        with conn.cursor() as cursor:
            # Usar una consulta parametrizada para evitar inyecciones SQL
            query = "SELECT * FROM Empleados WHERE NumEmpleado = %s"
            cursor.execute(query, (codigoEmpleado,))
            columns = [desc[0] for desc in cursor.description]
            result = cursor.fetchall()
            dict_results = [dict(zip(columns, row)) for row in result]
    finally:
        conn.close()
    return dict_results[0]