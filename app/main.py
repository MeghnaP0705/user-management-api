from fastapi import FastAPI, HTTPException
from app.models import User
from app import crud

app = FastAPI(title="User Management API")


@app.post("/users")
def create_user(user: User):
    return crud.create_user(user)


@app.get("/users")
def get_users():
    return crud.get_users()


@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    updated = crud.update_user(user_id, user)
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return updated


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    deleted = crud.delete_user(user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}
