from flask import Flask, request
from service import MainService

app = Flask(__name__)
service = MainService()

@app.route("/authorization", methods=["POST"])
def authorization():
    """
    Авторизация
    Поля, которые принимаются:
    - password - пароль пользователя
    - login - логин пользователя
    """
    req_fields = ["login", "password"]
    data = request.json
    if not all(map(lambda x: x in data, req_fields)):
        return {"error": f"invalid request. Required fields: {', '.join(req_fields)}"}

    user_login, user_password = data["login"], data["password"]
    result = service.authorization(user_login, user_password)
    if not result:
        return {"result": False}
    return {"result": True, "key": result["key"]}

@app.route("/registration", methods=["POST"])
def registration():
    """Регистрация"""
    req_fields = ["id", "login", "password", "name"]
    data = request.json
    print(list(map(lambda x: x in data, req_fields)))
    if not all(map(lambda x: x in data, req_fields)):
        return {"error": f"invalid request. Required fields: {', '.join(req_fields)}"}

    result = service.registration(data["id"], data["login"], data["password"], data["name"])
    if not result:
        return {"result": False}
    return {"result": True}


if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=False)
