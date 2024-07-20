from flask import Flask, request, render_template, redirect, url_for, flash
from flask_mysqldb import MySQL
import os
from werkzeug.utils import secure_filename
from flask import send_from_directory

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'bdflask'
app.config['UPLOAD_FOLDER'] = 'C:/Users/USUARIO/Downloads/pruebas flask/POO195/vistas/static/uploads' 
app.secret_key = 'mysecretkey'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg'}

mysql = MySQL(app)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.errorhandler(404)
def pagina_no_encontrada(e):
    return 'Revisa tu sintaxis: No encontré nada'

@app.route('/')
def index():
    try:
        with mysql.connection.cursor() as cursor:
            cursor.execute('SELECT * FROM albums')
            consultaA = cursor.fetchall()

        return render_template('index.html', albums=consultaA)
    except Exception as e:
        print(e)
        return 'Error al obtener los álbumes'

@app.route('/GuardarAlbum', methods=['POST'])
def guardarAlbum():
    if request.method == 'POST':
        Ftitulo = request.form['txtTitulo']
        Fartista = request.form['txtArtista']
        Fanio = request.form['txtAnio']
        file = request.files['portada']
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename)) # Guardar archivo en la ruta especificada
            
            cursor = mysql.connection.cursor()
            cursor.execute('INSERT INTO albums(titulo, artista, anio, portada) VALUES(%s, %s, %s, %s)', (Ftitulo, Fartista, Fanio, filename))
            mysql.connection.commit()
            flash('Álbum guardado correctamente', 'success')
        else:
            cursor = mysql.connection.cursor()
            cursor.execute('INSERT INTO albums(titulo, artista, anio, portada) VALUES(%s, %s, %s, %s)', (Ftitulo, Fartista, Fanio, None))
            mysql.connection.commit()
            flash('Error al guardar el álbum: ' + str(e), 'error')
        
        return redirect(url_for('index'))

@app.route('/editar/<id>')
def editar(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM albums WHERE idAlbum=%s', [id])
    albumE = cur.fetchone()
    return render_template('editar.html', album=albumE)

@app.route('/ActualizarAlbum/<id>', methods=['POST'])
def ActualizarAlbum(id):
    if request.method == 'POST':
        try:
            Ftitulo = request.form['txtTitulo']
            Fartista = request.form['txtArtista']
            Fanio = request.form['txtAnio']
            file = request.files['portada']
            
            cursor = mysql.connection.cursor()

            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                cursor.execute('UPDATE albums SET titulo=%s, artista=%s, anio=%s, portada=%s WHERE idAlbum=%s', (Ftitulo, Fartista, Fanio, filename, id))
            else:
                cursor.execute('UPDATE albums SET titulo=%s, artista=%s, anio=%s WHERE idAlbum=%s', (Ftitulo, Fartista, Fanio, id))
            
            mysql.connection.commit()
            flash('Álbum editado correctamente', 'info')
        
        except Exception as e:
            flash('Error al guardar el álbum: ' + str(e))
        
        return redirect(url_for('index'))  # Asegúrate de devolver una respuesta

@app.route('/eliminar/<int:id>')
def eliminar(id):
    try:
        with mysql.connection.cursor() as cur:
            cur.execute('DELETE FROM albums WHERE idAlbum = %s', [id])
            mysql.connection.commit()
        
        flash('Álbum eliminado correctamente', 'success')
        return redirect(url_for('index'))
    
    except Exception as e:
        flash('Error al eliminar el álbum: ' + str(e), 'error')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(port=14000, debug=True)
