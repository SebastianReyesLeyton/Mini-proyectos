from app import app
from flaskext.mysql import MySQL
from flask_jwt_extended import JWTManager
from os import environ

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = environ['MYSQLPASSWORD']
app.config['MYSQL_DATABASE_DB'] = 'UsersDB'
app.config['MYSQL_DATABASE_HOST'] = 'MySQLServiceDB'
app.config['MYSQL_DATABASE_PORT'] = 3306
mysql.init_app(app)