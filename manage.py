from app import create_app, db
from app.models import User



app = create_app('development')


if __name__ == '__main__':
    app.run()