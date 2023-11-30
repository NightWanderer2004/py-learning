from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/users")
async def get_users():
    return {"message": "Get all users"}


@app.get("/users/{user_id}")
async def get_user(user_id: int):
    return {"message": f"Get user with ID: {user_id}"}


@app.post("/users")
async def create_user():
    return {"message": "Create a new user"}


@app.put("/users/{user_id}")
async def update_user(user_id: int):
    return {"message": f"Update user with ID: {user_id}"}


@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    return {"message": f"Delete user with ID: {user_id}"}

