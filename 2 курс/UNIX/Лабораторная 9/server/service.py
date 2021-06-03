import os
import pickle
import hashlib
import json
import uuid


def md5_hash(text: str) -> str:
    """Хеширование данных по MD5"""
    hash_object = hashlib.md5(text.encode())
    return hash_object.hexdigest()


def keygen() -> str:
    """Генерация токена пользователя"""
    return str(uuid.uuid4()).replace("-", "")


class MainService:
    """Главный обработчик запросов"""

    def __init__(self, file_path: str = "./data.json") -> None:
        self.file_path = file_path
        self.__mydata = []
        self.reader()

    def reader(self):
        """Чтение данных"""
        with open(self.file_path, "r") as f:
            data = json.loads(f.read())
            if data is None or data == "": data = []
            self.__mydata = data

    def writer(self):
        """Запись данных"""
        with open(self.file_path, "w") as f:
            buffer = json.dumps(self.__mydata)
            f.write(buffer)

    def authorization(self, login: str, password: str):
        """Метод для авторизации пользователя в системе"""
        for item in self.__mydata:
            if item["login"] == login and item["password"] == md5_hash(password):
                return item
        return None

    def registration(self, my_id: int, login: str, password: str, name: str):
        """Метод регистрации пользователей"""
        # Хешируем пароль
        password = md5_hash(password)
        # Генерируем ключ
        key = keygen()
        data = {"id": my_id, "login": login, "password": password, "name": name, "key": key}
        self.__mydata.append(data)
        self.writer()
        return data
