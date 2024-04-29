from fastapi import FastAPI
from app import scrapper
from app import models

app = FastAPI(
    title="FIAP Tech Challenge API",
    description="Hello, there! This is an API built to retrieve data from Winemaking. "
                "Feel free to try out our endpoints"
)


@app.get('/', tags=['Hello, there!'])
def home():
    return ("Hello, there! Welcome to the first tech challenge delivered by Marcelo and Denise. Enjoy our API. (use "
            "'/docs' for documentation)")


@app.get('/producao/{first_year}:{last_year}', tags=['Get Data'],
         description="Returns a json with winemaking production data. "
                     "Use the params to define a time range or leave it blank to get the whole period",
         response_model=list[models.ProductionAndComercializationDTO]
         )
def get_data_producao(first_year, last_year):
    return scrapper.data_producao(first_year, last_year)


@app.get('/processamento/{first_year}:{last_year}', tags=['Get Data'],
         description="Returns a json with winemaking processing data "
                     "Use the params to define a time range or leave it blank to get the whole period",
         response_model=list[models.ProcessingDTO]
         )
def get_data_processamento(first_year=1970, last_year=0):
    return scrapper.data_processamento(first_year, last_year)


@app.get('/comercializacao/{first_year}:{last_year}', tags=['Get Data'],
         description="Returns a json with winemaking commercialization data "
                     "Use the params to define a time range or leave it blank to get the whole period",
         response_model=list[models.ProductionAndComercializationDTO]
         )
def get_data_processamento(first_year, last_year):
    return scrapper.data_comercializacao(first_year, last_year)


@app.get('/importacao/{first_year}:{last_year}', tags=['Get Data'],
         description="Returns a json with winemaking import data "
                     "Use the params to define a time range or leave it blank to get the whole period",
         response_model=list[models.ImportationAndExportationDTO]
         )
def get_data_importacao(first_year, last_year):
    return scrapper.data_importacao(first_year, last_year)


@app.get('/exportacao/{first_year}:{last_year}', tags=['Get Data'],
         description="Returns a json with winemaking export data "
                     "Use the params to define a time range or leave it blank to get the whole period",
         response_model=list[models.ImportationAndExportationDTO]
         )
def get_data_exportacao(first_year, last_year):
    return scrapper.data_exportacao(first_year, last_year)
