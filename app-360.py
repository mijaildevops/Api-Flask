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
@app.route ('/pais')
# New Branchs pais 
def GetDataPais():
    return 'Ruta Pais-Branch Created'

# //////////////////////////////////
@app.route ('/liga')
def GetDataLiga():
    return 'Ruta Liga'    

# //////////////////////////////////
@app.route ('/temporada')
def GetDataTemporada():
    return 'Ruta Temporada'    

# //////////////////////////////////
@app.route ('/categoria')
def GetDataCategoria():
    return 'Ruta categoria' 

# //////////////////////////////////
@app.route ('/noticias')
def GetDataNoticia():
    return 'Ruta notias' 

# //////////////////////////////////
@app.route ('/torneo')
def GetDataTorneo():
    return 'Ruta torneo' 

# //////////////////////////////////
@app.route ('/titulo')
def GetDataTitulo():
    return 'Ruta Titulo' 

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