from app import create_app
from app import db
from app.authentication.models import User

if __name__  == '__main__':
    flask_app = create_app('dev')

    with flask_app.app_context():
        db.create_all()
        if not User.query.filter_by(user_name = 'harry').first():
            User.create_user(user = 'harry',
                             email='harry_hogwarts@rowling.com',
                             password = 'secret')

    flask_app.run()