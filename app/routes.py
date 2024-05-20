from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.scrapper import data_importacao, data_producao, data_processamento, data_exportacao, data_comercializacao
from app.models import ProcessingDTO, ImportationAndExportationDTO, ProductionAndComercializationDTO
from app.auth_utils import create_access_token
from app.auth_utils import validate_token

user_router = APIRouter(dependencies=[Depends(validate_token)])
auth_router = APIRouter(prefix="/login")

@user_router.get('/producao/{first_year}:{last_year}', tags=['Get Data'],
            description="Returns a json with winemaking production data. "
                        "Use the params to define a time range or leave it blank to get the whole period",
            response_model=list[ProductionAndComercializationDTO]
            )
def get_data_producao(first_year, last_year):
    return data_producao(first_year, last_year)


@user_router.get('/processamento/{first_year}:{last_year}', tags=['Get Data'],
            description="Returns a json with winemaking processing data "
                        "Use the params to define a time range or leave it blank to get the whole period",
            response_model=list[ProcessingDTO]
            )
def get_data_processamento(first_year=1970, last_year=0):
    return data_processamento(first_year, last_year)


@user_router.get('/comercializacao/{first_year}:{last_year}', tags=['Get Data'],
            description="Returns a json with winemaking commercialization data "
                        "Use the params to define a time range or leave it blank to get the whole period",
            response_model=list[ProductionAndComercializationDTO]
            )
def get_data_processamento(first_year, last_year):
    return data_comercializacao(first_year, last_year)


@user_router.get('/importacao/{first_year}:{last_year}', tags=['Get Data'],
            description="Returns a json with winemaking import data "
                        "Use the params to define a time range or leave it blank to get the whole period",
            response_model=list[ImportationAndExportationDTO]
            )
def get_data_importacao(first_year, last_year):
    return data_importacao(first_year, last_year)


@user_router.get('/exportacao/{first_year}:{last_year}', tags=['Get Data'],
            description="Returns a json with winemaking export data "
                        "Use the params to define a time range or leave it blank to get the whole period",
            response_model=list[ImportationAndExportationDTO]
            )
def get_data_exportacao(first_year, last_year):
    return data_exportacao(first_year, last_year)


@auth_router.post('/token', tags=['Generate access token'])
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Implement validation of username and password

    access_token = create_access_token(data={"sub": form_data.username})
    return {"access_token": access_token[0], "token_type": "bearer", "expiration_date": access_token[1]}
