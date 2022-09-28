from typing import Protocol

# Protocol helps us to define signature of methods
# UserServiceProto is used to connect user_resource and user_service modules
# user_service must follow UserServiceProto contract
# info about Protocols : https://docs.python.org/3/library/typing.html#typing.Protocol


class UserServiceProto(Protocol):
    def save_user(self, name: str, surname: str, email: str, password: str) -> int:
        ...
