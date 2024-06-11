from flask import Flask, request,render_template, url_for, redirect, flash
from flask_mysqldb import MySQL


app = Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='bdflask'

app.secret_key='mysecretkey'

mysql= MySQL(app)

#Manejo de excepciones
@app.errorhandler(404)
def paginano (e):
    return 'Revisar tu sintaxis: No encontre nada'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/GuardarAlbum', methods=['POST'])
def guardarAlbum():
    if request.method == 'POST':
        
        #tomamos los daros que viene por POST
        Ftitulo=request.form['txtTitulo']
        Fartista=request.form['txtArtista']
        Fanio=request.form['txtAño']
        
        #enviamos a la BD
        
        cursor = mysql.connection.cursor()
        cursor.execute('insert into albums(titulo,artista,anio) values(%s,%s,%s)', (Ftitulo,Fartista,Fanio))
        mysql.connection.commit()
        flash('Album guardado correctamente')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(port=2000, debug= True)