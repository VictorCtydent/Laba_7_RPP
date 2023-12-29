import os
from __init__ import app
from __init__ import db
from app.routes import users


app.register_blueprint(users)


if __name__ == '__main__':
        with app.app_context():
            db.create_all()
        app.run(debug=True, host='0.0.0.0',port='4567')