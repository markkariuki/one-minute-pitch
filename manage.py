from app import create_app,db
from app.models import User

# Creating app instance
app = create_app('production')

manager = Manager(app)
manager.add_command('server', Server)
