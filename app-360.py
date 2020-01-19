from flask import Flask
from flask import jsonify
from flask_mysqldb import MySQL
import json
from flask import json

# //////////////////////////////////////////////////////////////
# Conexion a la BD
# SETTING
# //////////////////////////////////////////////////////////////
app = Flask(__name__)
app.config ['MYSQL_HOST'] = 'localhost'
app.config ['MYSQL_USER'] = 'Qatest'
app.config ['MYSQL_PASSWORD'] = 'Quito.2020'
app.config ['MYSQL_DB'] = 'world'
mysql = MySQL(app)

# //////////////////////////////////////////////////////////////
# Setting Rutas
# ////////////////////////////////////////////////////////////// 

# //////////////////////////////////
@app.route ('/data')
def getdata():
    #return 'Hello word'
    
    cur = mysql.connection.cursor()
    cur.execute('SELECT name, Continent, Region, HeadOfState FROM country')
    # la variable data es una lista, cada registro encontrado en la DB es una elemento de la lista 
    # un elemento de la lista puede tener N numero de propiedades (Columnas SELECT)
    data = cur.fetchall()
    print (json.dumps(data))


    return jsonify(
        # //////////////////////////////////////////////////////////////
        # un objeto json esta represantado entre llaves, todo lo que esta dentro de las llaves son propiedades del objeto 1
        # //////////////////////////////////////////////////////////////

        # //////////////////////////////////////////////////////////////
        # De esta forma se imprimer el primer Elemento o registro de la Lista con todas sus propiedades
        {"Paises": data[0], "message": "Forma de imprimir el primer Elemento o registro de la Lista con todas sus propiedades"},

        # //////////////////////////////////////////////////////////////
        # De esta forma se imprimer el primer Elemento o registro de la Lista, seleccionado solo una Propieded
        {"Pais": data[0][0], "message": "Forma de imprimir el primer Elemento o registro de la Lista, seleccionado solo una Propiedad"},
        
        # //////////////////////////////////////////////////////////////
        # De esta forma se Imprimen todos los registros
        {"Data": data, "message": "Forma de Imprimin todos los registros o Elementos"}
        )
    
# //////////////////////////////////////////////////////////////
# Setting Main Funtions
# configuracion de ambiente para hacer Deploy
# Setting Host dende se publica
# Setting Port
# Setting Debug Opcion, para que cada vez que se hace save Aplique un reload
# ////////////////////////////////////////////////////////////// 
if __name__ == '__main__':
     app.run(port = 5080, debug = True, host='192.168.100.233') # PC Main
    # app.run(port = 4321, debug = True, host='192.168.100.156') # Laptop