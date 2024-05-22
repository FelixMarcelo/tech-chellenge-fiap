from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from app.scrapper import data_importacao, data_producao, data_processamento, data_exportacao, data_comercializacao
from app.models import ProcessingDTO, ImportationAndExportationDTO, ProductionAndComercializationDTO
from app.auth_utils import UserUseCases
from app.depends import get_db_session, token_verifier
from sqlalchemy.orm import Session
from app.schemas import User

user_router = APIRouter(dependencies=[Depends(token_verifier)])
auth_router = APIRouter()


@auth_router.post('/register', tags=["Authentication"],
                  description="User register. For security purposes, you need to be registered in our database to use "
                              "this API")
async def user_register(
        user: User,
        db_session: Session = Depends(get_db_session)
):
    uc = UserUseCases(db_session=db_session)
    uc.user_register(user=user)
    return JSONResponse(
        content={'msg': 'Registration done successfully.'},
        status_code=status.HTTP_201_CREATED
    )


@auth_router.post('/login', tags=["Authentication"],
                  description="If the user is registered, returns a auth token that gives access to all API endpoints")
async def user_login(
        request_form_user: OAuth2PasswordRequestForm = Depends(),
        db_session: Session = Depends(get_db_session)
):
    uc = UserUseCases(db_session=db_session)
    user = User(
        username=request_form_user.username,
        password=request_form_user.password
    )
    auth_data = uc.user_login(user)
    return JSONResponse(
        content=auth_data,
        status_code=status.HTTP_200_OK
    )


@user_router.get('/producao/{first_year}:{last_year}', tags=['Get Data'],
                 description="Returns a json with winemaking production data. "
                             "Use the params to define a time range or leave it blank to get the whole period",
                 response_model=list[ProductionAndComercializationDTO]
                 )
async def get_data_producao(first_year=1980, last_year=1980):
    return data_producao(first_year, last_year)


@user_router.get('/processamento/{first_year}:{last_year}', tags=['Get Data'],
                 description="Returns a json with winemaking processing data "
                             "Use the params to define a time range or leave it blank to get the whole period",
                 response_model=list[ProcessingDTO]
                 )
async def get_data_processamento(first_year: int, last_year: int):
    return data_processamento(first_year, last_year)


@user_router.get('/comercializacao/{first_year}:{last_year}', tags=['Get Data'],
                 description="Returns a json with winemaking commercialization data "
                             "Use the params to define a time range or leave it blank to get the whole period",
                 response_model=list[ProductionAndComercializationDTO]
                 )
async def get_data_processamento(first_year: int, last_year: int):
    return data_comercializacao(first_year, last_year)


@user_router.get('/importacao/{first_year}:{last_year}', tags=['Get Data'],
                 description="Returns a json with winemaking import data "
                             "Use the params to define a time range or leave it blank to get the whole period",
                 response_model=list[ImportationAndExportationDTO]
                 )
async def get_data_importacao(first_year: int, last_year: int):
    return data_importacao(first_year, last_year)


@user_router.get('/exportacao/{first_year}:{last_year}', tags=['Get Data'],
                 description="Returns a json with winemaking export data "
                             "Use the params to define a time range or leave it blank to get the whole period",
                 response_model=list[ImportationAndExportationDTO]
                 )
async def get_data_exportacao(first_year: int, last_year: int):
    return data_exportacao(first_year, last_year)
