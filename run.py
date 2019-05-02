from app import create_app
from app import db
from app.authentication.models import User
from sqlalchemy import exc

flask_app = create_app('prod')

with flask_app.app_context():
    db.create_all()

    try:
        if not User.query.filter_by(user_name = 'sherlock holmes').first():
                    User.create_user(user = 'sherlock holmes',
                                    email='sherlock_holmes@gmail.com',
                                    password = 'secret')
    except:
        exc.IntegretiyError


    flask_app.run()