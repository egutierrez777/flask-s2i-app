from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "¡Hola desde Flask en OpenShift con S2I!"

@app.route('/hello/<name>')
def greet(name):
    return f"Hola {name}, ¡Bienvenido a OpenShift!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
