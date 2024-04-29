from pydantic import BaseModel


class ProductionAndComercializationDTO(BaseModel):
    ano: str
    produto: str
    categoria: str
    quantidade: str

    def __init__(self, ano: str, produto: str, categoria: str, quantidade: str):
        super().__init__(ano=ano, produto=produto, categoria=categoria, quantidade=quantidade)


class ProcessingDTO(BaseModel):
    ano: str
    cultivar: str
    categoria: str
    quantidade: str

    def __init__(self, ano: str, cultivar: str, categoria: str, quantidade: str):
        super().__init__(ano=ano, cultivar=cultivar, categoria=categoria, quantidade=quantidade)


class ImportationAndExportationDTO(BaseModel):
    ano: str
    paises: str
    quantidade: str
    valor: str

    def __init__(self, ano: str, paises: str, quantidade: str, valor: str):
        super().__init__(ano=ano, paises=paises, quantidade=quantidade, valor=valor)