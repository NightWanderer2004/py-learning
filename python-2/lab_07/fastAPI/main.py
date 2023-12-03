from fastapi import FastAPI
from models import User

app = FastAPI()

users = []

@app.get("/users")
async def get_users():
    return users

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    if 1 <= user_id <= len(users):
        return users[user_id - 1]
    else:
        return {"message": f"User with ID {user_id} doesn't exist"}

@app.post("/users")
async def create_user(user: User):
    users.append(user)
    return {"message": "User created successfully"}

@app.put("/users/{user_id}")
async def update_user(user_id: int, updated_user: User):
    if 1 <= user_id <= len(users):
        users[user_id - 1] = updated_user
        return {"message": f"User with ID {user_id} updated successfully"}
    else:
        return {"message": f"User with ID {user_id} doesn't exist"}

@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    if 1 <= user_id <= len(users):
        users.pop(user_id - 1)
        return {"message": f"User with ID {user_id} deleted successfully"}
    else:
        return {"message": f"User with ID {user_id} doesn't exist"}
