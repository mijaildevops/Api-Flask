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
    data = cur.fetchall()
    print (json.dumps(data))
    #return jsonify (data)
    #print (json.dumps(data))

    return jsonify(
        # esto es un arrecglo de Ob
        # un objeto json esta represantado entre llaves, todo lo que esta dentro de las llaves son propiedades del objeto 1
        # para selecionar 
        {"Data": data[0][1], "message": "Lista de db"},
        {"Data": data[1], "message": "Lista de db"},
        {"Data": data[2], "message": "Lista de db"},
        {"Data": data[3], "message": "Lista de db"},
        {"Data": data[4], "message": "Lista de db"}
        )
    
# //////////////////////////////////////////////////////////////
# Setting Main Funtions
# ////////////////////////////////////////////////////////////// 
if __name__ == '__main__':
     app.run(port = 4321, debug = True, host='192.168.100.233') # PC Main
    # app.run(port = 4321, debug = True, host='192.168.100.156') # Laptop