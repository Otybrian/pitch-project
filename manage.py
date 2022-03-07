# from multiprocessing import managers
from app import create_app, db
from app.models import User, Role
# from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Server





app = create_app('development')
manager = Manager(app)
manager.add_command('server', Server)

@manager.shell
def make_shell_context():
    return dict(app = app, db = db, Role = Role, User = User)


if __name__ == '__main__':
    manager.run()