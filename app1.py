from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app1 = Flask(__name__)


app1.config['MYSQL_HOST']= 'localhost'
app1.config['MYSQL_USER']= 'root'
app1.config['MYSQL_PASSWORD']= ''
app1.config['MYSQL_DB']= 'yoga'
mysql= MySQL(app1)


@app1.route('/')
def Homepage():
    return render_template('index.html')

@app1.route('/Login',methods=['GET','POST'])
def Login():
		if request.method == 'POST':
			email = request.form['Email']
			password = request.form['Password']
			cur = mysql.connection.cursor()
			cur.execute('INSERT INTO login (Email,Password) VALUES (%s, %s)', (email, password))
			mysql.connection.commit()
			cur.close()
			return render_template('Yoga.html')
		return render_template('Login.html')
		
		
 
@app1.route('/SignUp',methods=['GET','POST'])
def SignUp():
	if request.method == 'POST':
		name = request.form['Name']
		email = request.form['Email']
		password = request.form['Password']
		course = request.form['Course']
		cur = mysql.connection.cursor()
		cur.execute('INSERT INTO signup (Name,Email,Password,Course) VALUES (%s, %s, %s, %s)', (name,email, password,course))
		mysql.connection.commit()
		cur.close()
		return render_template('index.html')
	return render_template('SignUp.html')

@app1.route('/Login/Yoga')
def Yoga():
    return render_template('Yoga.html')


if __name__ == "__main__":
    app1.run(debug=True,)