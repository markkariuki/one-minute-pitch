from flask_sqlachemy import SQLAlchemy


bootstrap = Bootstrap()
db = SQLAlchemy()

def create app(config_name):
    app = Flask(__name__)



    bootstrap.init_app(app)
    db.init_app(app)
