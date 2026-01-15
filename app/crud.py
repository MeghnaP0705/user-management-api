from typing import Dict
from app.models import User

users_db: Dict[int, User] = {}
user_id_counter = 1


def create_user(user: User) -> dict:
    global user_id_counter
    users_db[user_id_counter] = user
    user_id_counter += 1
    return {"id": user_id_counter - 1, **user.model_dump()}


def get_users():
    return [{"id": uid, **user.model_dump()} for uid, user in users_db.items()]


def update_user(user_id: int, user: User):
    if user_id not in users_db:
        return None
    users_db[user_id] = user
    return {"id": user_id, **user.model_dump()}


def delete_user(user_id: int):
    return users_db.pop(user_id, None)
