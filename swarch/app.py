from flask import Flask 
from config import DB_CONFIG 
from models.grade import db 
from controllers.grade_controller import grade_bp 
import time
from sqlalchemy.exc import OperationalError

app = Flask(__name__) 

app.config.update(DB_CONFIG) 

db.init_app(app)

app.register_blueprint(grade_bp) 

if __name__ == '__main__':
    with app.app_context():
        retries = 5
        while retries > 0:
            try:
                db.create_all() # Línea 138 del PDF
                print("Conexión exitosa a la base de datos")
                break
            except OperationalError:
                retries -= 1
                print(f"Esperando a la base de datos... quedan {retries} intentos")
                time.sleep(5)
        
        app.run(host='0.0.0.0', port=5000, debug=True)