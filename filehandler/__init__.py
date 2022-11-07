from flask import Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///file.db'
from src.db import db
db.init_app(app)
with app.app_context():
        db.create_all()
import src.routes.routes