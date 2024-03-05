from dao.base_dao import BaseDAO
from model.user_model import User


class UserDAO(BaseDAO):
    def __init__(self):
        super().__init__()

    def get_user(self, user_name):
        cursor = self.query("SELECT * FROM users where user_name = " + user_name, None)
        rs = cursor.fetchone()
        user = User(id=rs[0], name=rs[1], password=rs[2], email=rs[3])
        return user

    def get_all_users(self):
        users = []
        cursor = self.query("SELECT * FROM users", None)
        results = cursor.fetchall()
        for rs in results:
            user = User(id=rs[0], name=rs[1], password=rs[2], email=rs[3])
            users.append(user)
        return users

    def create_user(self, user):
        sql = "INSERT INTO users (name, password, email) VALUES (%s, %s, %s)"
        val = (user.name, user.password, user.email)
        cursor = self.query(sql, val)
        self.commit()
        user.id = cursor.lastrowid
        return user

    def delete_user_by_id(self, user_id: int):
        sql = "DELETE FROM users WHERE id = %s"
        val = (user_id,)
        cursor = self.query(sql, val)
        self.commit()

    def delete_user_by_name(self, user_name: str):
        sql = "DELETE FROM users WHERE name = %s"
        val = (user_name,)
        cursor = self.query(sql, val)
        self.commit()
