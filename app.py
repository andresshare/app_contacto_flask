from flask import Flask, render_template, request, redirect,url_for,flash
from flask_mysqldb import MySQL


app = Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='user360'
app.config['MYSQL_PASSWORD']='8010Andres*'
app.config['MYSQL_DB']='db_contacto_flask'

mysql = MySQL(app)

#SETTINGS
app.secret_key = 'mysecretkey'



@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * from contacts')
    data = cur.fetchall()
    print(data)
    return render_template('index.html',contacts = data)


@app.route('/add_contact',methods=['POST'])
def contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']

        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO contacts (fullname,phone,email) VALUES (%s,%s,%s)',
                    (fullname, phone, email))

        mysql.connection.commit()

        flash('contact added SUCCESSFULLY')
        return redirect(url_for('index'))


    return 'añadir contacto'


@app.route('/edit')
def edit_contact():
    return 'edit contact'

@app.route('/delete')
def delete_contact():
    return 'delete contact'


if __name__ == '__main__':
    app.run(port  =  3000, debug=True)


