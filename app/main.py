from fastapi import FastAPI
from app.routes import user_router, auth_router

app = FastAPI(
    title="FIAP Tech Challenge API",
    description="Hello, there! This is an API built to retrieve data from Winemaking. "
                "Feel free to try out our endpoints"
)


@app.get('/', tags=['Hello, there!'])
def home():
    return ("Hello, there! Welcome to the first tech challenge delivered by Marcelo and Denise. Enjoy our API. (use "
            "'/docs' for documentation)")


app.include_router(router=user_router)
app.include_router(router=auth_router)

