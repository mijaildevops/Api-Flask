from flask import Flask, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = '192.168.100.51'
app.config['MYSQL_USER'] = 'Qatest'
app.config['MYSQL_PASSWORD'] = 'Quito.2019'
app.config['MYSQL_DB'] = 'Automatizacion'
mysql = MySQL(app)


@app.route ('/')
def Index():
    #return 'Hello word'
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM record')
    data = cur.fetchall()
    return jsonify (data[0])


if __name__ == '__main__':
    # app.run(port = 4321, debug = True, host='192.168.100.233') # PC Main
    app.run(port = 4321, debug = True, host='192.168.100.156') # Laptop