from flask import Flask

app = Flask(__name__)
@app.route('/')
def hola():
    return "<h1>¡Hola Pablo Andrés Landeta López! Ejemplo de CI/CD hacia Docker en instancia EC2</h1>"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
