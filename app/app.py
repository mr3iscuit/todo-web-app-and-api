from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from api.routers import todo, user

app = FastAPI()
app.include_router(todo.router)
app.include_router(user.router)

register_tortoise(
    app                    = app,
    db_url                 = "sqlite://todo.db",
    add_exception_handlers = True,
    generate_schemas       = True,

    modules = { "models": ["api.models.todo", "api.models.user"] }
)

@app.get('/')
def index():
    return "Home Page"
