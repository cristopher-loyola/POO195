from flask import Flask, request,render_template
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='bdflask'

mysql = MySQL(app)

# Manejo de excepciones
@app.errorhandler(404)
def paginano(e):
    return 'Revisar tu sintaxis: No encontré nada'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/GuardarAlbum', methods=['POST'])
def guardarAlbum():
    if request.method == 'POST':
        titulo=request.form['txtTitulo']
        artista=request.form['txtArtista']
        año=request.form['txtAño']
        print(titulo,artista,año)
        return 'Datos recibidos en el server'

if __name__ == '__main__':
    app.run(port=2000, debug=True)
