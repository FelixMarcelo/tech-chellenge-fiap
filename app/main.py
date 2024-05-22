from fastapi import FastAPI
from app.routes import user_router, auth_router

description = """
## Hello, there! This is a REST API built to retrieve data from Winemaking. Feel free to try our endpoints
### First things first. Please register your self and then click on the 'Authorize' button on your right to login.

Obs: If you want to try this API on insomnia or postman you can create a Bearer token using the /login endpoint.

"""

app = FastAPI(
    title="FIAP Tech Challenge API",
    description=description
)


@app.get('/', tags=['Home'])
def home():
    return ("Hello, there! Welcome to the first tech challenge delivered by Marcelo and Denise. Enjoy our API. (use "
            "'/docs' for documentation)")


app.include_router(router=user_router)
app.include_router(router=auth_router)

