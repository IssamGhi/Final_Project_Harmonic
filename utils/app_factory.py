from flask import Flask
from flask_injector import FlaskInjector, request
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_swagger import swagger

from utils.config import postgresql_string,postgresql_string_test
from repositories.mock_repository import MockRepository
from repositories.genric_repository import GenericRepository
from repositories.user_repository import UserRepository
from repositories.issue_repository import IssueRepository
from services.user_service import UserService
from services.issue_service import IssueService
from resources.user_resource import UserResource
from resources.issue_resource import IssueResource
from resources.login_resource import LoginResource
from utils.database import db
import jsonify

def create_app(config):


    app = Flask(__name__)

    ##Ajouter la configuration postgres à notre app
    if config["MODE"] == "TEST":
        app.config['SQLALCHEMY_DATABASE_URI'] =postgresql_string_test
        app.config["JWT_SECRET_KEY"] = "une clé secrete pour générer le jwt en mode test"
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = postgresql_string
        app.config["JWT_SECRET_KEY"] = "une clé secrete pour générer le jwt en mode prod"

    ##Créer notre JWTManager pour notre application
    jwt = JWTManager(app)

    ##Création de l'api et l'ajout des ressources, Api de flask restful est un middleware (A avoir dans en detail dans la prtie sécurité)
    api = Api(app)

    @app.before_first_request
    def initialize_db():
        db.init_app(app)
        db.create_all()

    ##ressources user, login
    api.add_resource(UserResource, '/users/register',  endpoint='users')
    #api.add_resource(UserResource, '/users/<int::id>',  endpoint='users')
    api.add_resource(LoginResource, '/users/login',  endpoint='login')
    api.add_resource(IssueResource, '/issues', endpoint='issues')

    ##Ajouter une route pour la documentation swagger
    @app.route('/doc')
    def doc():
        return jsonify(swagger(app))

    def flask_injector_configuration(binder):
        binder.bind(GenericRepository, to=GenericRepository, scope=request)
        binder.bind(UserService, to=UserService, scope=request)
        binder.bind(UserRepository, to=UserRepository, scope=request)
        binder.bind(MockRepository, to=MockRepository, scope=request)
        binder.bind(IssueRepository, to=IssueRepository, scope=request)
        binder.bind(IssueService, to=IssueService, scope=request)

    FlaskInjector(app=app, modules=[flask_injector_configuration])
    return app