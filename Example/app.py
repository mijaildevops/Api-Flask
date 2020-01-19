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
# Get Data desde archivo Externo "products.py"
# //////////////////////////////////////////////////////////////
from products import products

# //////////////////////////////////////////////////////////////
# Setting Rutas
# ////////////////////////////////////////////////////////////// 

# //////////////////////////////////
@app.route ('/Data')
def getdata():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM performance order by id desc LIMIT 5')
    data = cur.fetchall()
    print (json.dumps(data))
    
    #datas = (json.dumps(data))
    return jsonify(
        {"Data": data[0], "message": "Lista de db"},
        {"Data": data[1], "message": "Lista de db"},
        {"Data": data[2], "message": "Lista de db"},
        {"Data": data[3], "message": "Lista de db"},
        {"Data": data[4], "message": "Lista de db"}
        )
    
# //////////////////////////////////
@app.route('/test')
def test():
    return 'Pagina test API-REST'

# //////////////////////////////////
@app.route ('/products')
def getproducts():
    return jsonify({"products": products, "message": "Lista de Productos"})

# //////////////////////////////////////////////////////////////
# Setting Main Funtions
# ////////////////////////////////////////////////////////////// 
if __name__ == '__main__':
    app.run(debug=True, port=4320)