from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
 
db = SQLAlchemy() 
 

def create_app():
   

    app = Flask(__name__)

    app.config.from_object("app.config.Config")

    db.init_app(app)

    from app.routes.emp_routes import emp_bp
    app.register_blueprint(emp_bp)
    @app.route("/test")
    def test():
        return "working"

    return app