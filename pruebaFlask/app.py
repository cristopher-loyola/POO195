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
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM albums')
        consultaA = cursor.fetchall()
        print(consultaA)
        return render_template('index.html', albums=consultaA)
    except Exception as e:
        print(f"Error al realizar la consulta en la tabla albums: {e}")
        return render_template('index.html', albums=[])

@app.route('/registro', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        try:
            Fnombre = request.form['txtNombre']
            Frfc = request.form['txtRfc']
            Fcedula = request.form['txtCedula']
            Fcorreo = request.form['txtCorreo']
            Fcontraseña = request.form['txtContraseña']
            Frol = request.form['txtRol']
            
            cursor = mysql.connection.cursor()
            cursor.execute('INSERT INTO tbmedicos (nombre, rfc, cedulaP, correoE, contraseña, rol) VALUES (%s, %s, %s, %s, %s, %s)', 
                           (Fnombre, Frfc, Fcedula, Fcorreo, Fcontraseña, Frol))
            mysql.connection.commit()
            flash('Médico registrado correctamente')
            return redirect(url_for('consultas')) 
        except Exception as e:
            print(f"Error al registrar el médico: {e}")
            flash('Error al registrar el médico: ' + str(e))
            return redirect(url_for('formulario'))  
    
    return render_template('GuardarAlbum.html')



@app.route('/consultas')
def consultas():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM tbmedicos')
        consultaA = cursor.fetchall()
        print(consultaA)
        return render_template('consultaMedicos.html',view='ConsultaMedicos', medicos=consultaA)
    except Exception as e:
        print(f"Error al realizar la consulta en la tabla tbmedicos: {e}")
        
        


if __name__ == '__main__':
    app.run(port=9000, debug=True)
