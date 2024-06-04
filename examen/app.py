from flask import Flask, request,render_template



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/formulario')
def formulario():
    return render_template('formulario.html')

@app.route('/numeroalcuadrado/<int:numero>', methods=['GET'])
def numeroalcuadrado(numero):
    resultado = numero ** 2
    return render_template('resultado.html', numero=numero, resultado=resultado)

@app.errorhandler(404)
def paginano(e):
    return "Ruta no encontrada. Por favor, verifique la URL.", 404


if __name__ == '__main__':
    app.run(port=2000, debug= True)
    

