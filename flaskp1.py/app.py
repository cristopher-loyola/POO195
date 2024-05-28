from flask import Flask, request

# Se crea una instancia de Flask, que es la aplicación web.
app = Flask(__name__)

# Ruta simple
@app.route('/')
def principal():
    return 'Hola Mundo flask'

@app.route('/usuario')
@app.route('/saludar')
def saludos():
    return 'Cristopher Antonio Loyola Martinez'

#rutas con parametros
@app.route('/hi/<nombre>')
def hi(nombre):
    return 'Hola '+ nombre + '!!!'

#definicion de metodos de trabajo
@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    if request.method == 'GET':
        return 'No es seguro enviar password por GET'
    elif request.method == 'POST':
        return 'POST si es seguro para pasar'

#Manejo de excepciones
@app.errorhandler(404)
def paginano (e):
    return 'Revisar tu sintaxis: No encontre nada'



if __name__ == '__main__':
    # port es el puerto donde se ejecutará la aplicación y debug=True activa el modo de depuración.
    app.run(port=3000, debug=True)
