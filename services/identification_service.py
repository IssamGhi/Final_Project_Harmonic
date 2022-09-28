from flask_jwt_extended import create_access_token


class IdentificationService:

    def login(self, email, password):
        if email=="dilek@" and password =="blackcat":
            token = create_access_token("dilek@", additional_claims={"role":"admin"})
            return token
        else:
            raise ValueError("Erreur email ou password")




