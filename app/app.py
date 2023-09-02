from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from api.routers import todo

app = FastAPI()
app.include_router(todo.router)

register_tortoise(
    app                    = app,
    db_url                 = "sqlite://todo.db",
    add_exception_handlers = True,
    generate_schemas       = True,

    modules = { "models": ["api.models.todo"] }
)

@app.get('/')
def index():
    return "Home Page"
