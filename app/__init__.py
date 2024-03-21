from flask import Flask
from app.extensions import db,migrate,bcrypt
from app.contollers.auth.auth_controller import auth

#application factory function
def create_app():
    
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    
    db.init_app(app)
    migrate.init_app(app,db)
    bcrypt.init_app(app)
    
    #importing and registering models
    from app.models.users import User
#     from app.models.companies import Company
#     from app.models.books import Books
    
    
    
    @app.route("/")
    def home():
            return "Hello World!"
    
    #register blueprints
    app.register_blueprint(auth, url_prefix='/api/v1/auth/')
    
        
        
    return app
        
    