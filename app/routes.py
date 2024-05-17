from fastapi import APIRouter
from app.scrapper import data_importacao, data_producao, data_processamento, data_exportacao, data_comercializacao
from app.models import ProcessingDTO, ImportationAndExportationDTO, ProductionAndComercializationDTO

router = APIRouter()


@router.get('/producao/{first_year}:{last_year}', tags=['Get Data'],
            description="Returns a json with winemaking production data. "
                        "Use the params to define a time range or leave it blank to get the whole period",
            response_model=list[ProductionAndComercializationDTO]
            )
def get_data_producao(first_year, last_year):
    return data_producao(first_year, last_year)


@router.get('/processamento/{first_year}:{last_year}', tags=['Get Data'],
            description="Returns a json with winemaking processing data "
                        "Use the params to define a time range or leave it blank to get the whole period",
            response_model=list[ProcessingDTO]
            )
def get_data_processamento(first_year=1970, last_year=0):
    return data_processamento(first_year, last_year)


@router.get('/comercializacao/{first_year}:{last_year}', tags=['Get Data'],
            description="Returns a json with winemaking commercialization data "
                        "Use the params to define a time range or leave it blank to get the whole period",
            response_model=list[ProductionAndComercializationDTO]
            )
def get_data_processamento(first_year, last_year):
    return data_comercializacao(first_year, last_year)


@router.get('/importacao/{first_year}:{last_year}', tags=['Get Data'],
            description="Returns a json with winemaking import data "
                        "Use the params to define a time range or leave it blank to get the whole period",
            response_model=list[ImportationAndExportationDTO]
            )
def get_data_importacao(first_year, last_year):
    return data_importacao(first_year, last_year)


@router.get('/exportacao/{first_year}:{last_year}', tags=['Get Data'],
            description="Returns a json with winemaking export data "
                        "Use the params to define a time range or leave it blank to get the whole period",
            response_model=list[ImportationAndExportationDTO]
            )
def get_data_exportacao(first_year, last_year):
    return data_exportacao(first_year, last_year)
