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
    try:
        cursor= mysql.connection.cursor();
        cursor.execute('select * from albums')
        consultaA = cursor.fetchall()
        print(consultaA)
        return render_template('index.html')
    except Exception as e:
        print(e)
        


@app.route('/registro', methods=['GET', 'POST'])
def formulario():
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
            cursor.execute('INSERT INTO tbmedicos (nombre, rfc, cedulaP, correoE, contraseña, rol) VALUES (%s, %s, %s, %s, %s, %s)', (Fnombre, Frfc, Fcedula, Fcorreo, Fcontraseña, Frol))
            mysql.connection.commit()
            flash('Médico registrado correctamente')
            return redirect(url_for('home'))
        except Exception as e:
            flash('Error al registrar el médico: ' + str(e))
            return redirect(url_for('formulario'))
    return render_template('GuardarAlbum.html')

if __name__ == '__main__':
    app.run(port=2000, debug=True)

