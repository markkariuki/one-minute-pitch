from app import create_app,db
from app.models import User

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,user = user )

if __name__ == '__main__':
    manager.run
