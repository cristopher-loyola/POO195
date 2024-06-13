from flask import Flask, request, render_template, url_for, redirect, flash
from flask_mysqldb import MySQL


app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'tbmedicos'

app.secret_key = 'mysecretkey'  


mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/registro')
def formulario():
    return render_template('GuardarAlbum.html')
def guardarMedico():
    if request.method == 'POST':
        try:
            # Tomamos los datos que vienen por POST
            Fnombre = request.form['txtNombre']
            Frfc = request.form['txtRfc']
            Fcedula = request.form['txtCedula']
            Fcorreo = request.form['txtCorreo']
            Fcontraseña = request.form['txtContraseña']
            Frol = request.form['txtRol']
            
            # Enviamos a la BD
            cursor = mysql.connection.cursor()
            cursor.execute('INSERT INTO medicos(nombre, rfc, cedula_profesional, correo, contraseña, rol) VALUES(%s, %s, %s, %s, %s, %s)', (Fnombre, Frfc, FcedulaP, FcorreoE, Fcontraseña, Frol))
            mysql.connection.commit()
            flash('Médico registrado correctamente')
            return redirect(url_for('index'))
        except Exception as e:
            flash('Error al registrar el médico: ' + str(e))
            return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(port=2000, debug=True)

