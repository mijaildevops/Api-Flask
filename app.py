from flask import Flask

app = Flask(__name__)

@app.route ('/')
def Index():
    return 'Hello word'

if __name__ == '__main__':
    app.run(port = 4321, debug = True, host='192.168.100.233')