from bs4 import BeautifulSoup as Soup
import requests
import re
from app import models
from fastapi import HTTPException, status

url_base = "http://vitibrasil.cnpuv.embrapa.br/index.php?"
url_year = "ano="
url_opt = "&opcao=opt_0"


def headers():
    agent_headers = requests.utils.default_headers()
    agent_headers.update(
        {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                       'Chrome/98.0.4758.102 Safari/537.36'}
    )
    return agent_headers


def _find_final_year(final_year: int):
    request = requests.get(f'{url_base}{url_opt}{final_year}',
                           headers=headers())
    html = Soup(request.content, 'html.parser')
    text = html.find('p', class_='text_center').text.strip()
    year = int(re.findall(r'\d+', text)[0])

    return year


def _reset_initial_params(first_year, last_year, final_year):
    if first_year == "{first_year}":
        first_year = 1970
    if last_year == "{last_year}":
        last_year = final_year

    try:
        first_year = int(first_year)
        last_year = int(last_year)
    except (ValueError, TypeError):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="You need to pass numeric values as params."
        )

    _validate_time_range(first_year, last_year, final_year)

    return first_year, last_year, final_year


def _validate_time_range(first_year: int, last_year: int, final_year: int):
    if (first_year < 1970) | (last_year > final_year):
        raise HTTPException(
            status_code=400,
            detail=f"Sorry, we only have data from 1970 to {final_year}. But don't worry, try again "
                   "using a period between those dates"
        )


def data_producao(first_year, last_year):
    opt = 2
    final_year = _find_final_year(opt)
    data = []

    first_year, last_year, final_year = _reset_initial_params(first_year, last_year, final_year)

    for y in range(first_year, last_year + 1):
        request = requests.get(f'{url_base}{url_year}{y}{url_opt}{opt}',
                               headers=headers())
        html = Soup(request.content, 'html.parser')
        table = html.find_all("table", class_="tb_base tb_dados")
        lines = table[0].find_all('tr')
        category = ""
        text = html.find('p', class_='text_center').text.strip()
        year = re.findall(r'\d+', text)[0]
        for line in lines:
            tb_item = line.find_all('td', class_='tb_item')
            tb_subitem = line.find_all('td', class_='tb_subitem')
            if len(tb_item) >= 1:
                category = tb_item[0].text.strip()
            if len(tb_subitem) >= 1:
                product = tb_subitem[0].text.strip()
                quantity = tb_subitem[1].text.strip()
                item = models.ProductionAndComercializationDTO(year, product, category, quantity)
                data.append(item)

    return data


def data_processamento(first_year, last_year):
    opt = 3
    final_year = _find_final_year(opt)
    data = []

    first_year, last_year, final_year = _reset_initial_params(first_year, last_year, final_year)

    for y in range(first_year, last_year + 1):
        request = requests.get(f'{url_base}{url_year}{y}{url_opt}{opt}',
                               headers=headers())
        html = Soup(request.content, 'html.parser')
        table = html.find_all("table", class_="tb_base tb_dados")
        lines = table[0].find_all('tr')
        category = ""
        text = html.find('p', class_='text_center').text.strip()
        year = re.findall(r'\d+', text)[0]
        for line in lines:
            tb_item = line.find_all('td', class_='tb_item')
            tb_subitem = line.find_all('td', class_='tb_subitem')
            if len(tb_item) >= 1:
                category = tb_item[0].text.strip()
            if len(tb_subitem) >= 1:
                product = tb_subitem[0].text.strip()
                quantity = tb_subitem[1].text.strip()
                item = models.ProcessingDTO(year, product, category, quantity)
                data.append(item)

    return data


def data_comercializacao(first_year, last_year):
    opt = 4
    final_year = _find_final_year(opt)
    data = []

    first_year, last_year, final_year = _reset_initial_params(first_year, last_year, final_year)

    for y in range(first_year, last_year + 1):
        request = requests.get(f'{url_base}{url_year}{y}{url_opt}{opt}',
                               headers=headers())
        html = Soup(request.content, 'html.parser')
        table = html.find_all("table", class_="tb_base tb_dados")
        lines = table[0].find_all('tr')
        category = ""
        text = html.find('p', class_='text_center').text.strip()
        year = re.findall(r'\d+', text)[0]
        for line in lines:
            tb_item = line.find_all('td', class_='tb_item')
            tb_subitem = line.find_all('td', class_='tb_subitem')
            if len(tb_item) >= 1:
                category = tb_item[0].text.strip()
            if len(tb_subitem) >= 1:
                product = tb_subitem[0].text.strip()
                quantity = tb_subitem[1].text.strip()
                item = models.ProductionAndComercializationDTO(year, product, category, quantity)
                data.append(item)

    return data


def data_importacao(first_year, last_year):
    opt = 5
    final_year = _find_final_year(opt)
    data = []

    first_year, last_year, final_year = _reset_initial_params(first_year, last_year, final_year)

    for y in range(first_year, last_year + 1):
        request = requests.get(f'{url_base}{url_year}{y}{url_opt}{opt}',
                               headers=headers())
        html = Soup(request.content, 'html.parser')
        table = html.find_all("table", class_="tb_base tb_dados")
        lines = table[0].find_all('tr')
        text = html.find('p', class_='text_center').text.strip()
        year = re.findall(r'\d+', text)[0]
        for line in lines:
            tb_item = line.find_all('td')
            if len(tb_item) >= 1:
                countries = tb_item[0].text.strip()
                quantity = tb_item[1].text.strip()
                value = tb_item[2].text.strip()
                if countries != "Total":
                    item = models.ImportationAndExportationDTO(year, countries, quantity, value)
                    data.append(item)

    return data


def data_exportacao(first_year, last_year):
    opt = 6
    final_year = _find_final_year(opt)
    data = []

    first_year, last_year, final_year = _reset_initial_params(first_year, last_year, final_year)

    for y in range(first_year, last_year + 1):
        request = requests.get(f'{url_base}{url_year}{y}{url_opt}{opt}',
                               headers=headers())

        html = Soup(request.content, 'html.parser')
        table = html.find_all("table", class_="tb_base tb_dados")
        lines = table[0].find_all('tr')
        text = html.find('p', class_='text_center').text.strip()
        year = re.findall(r'\d+', text)[0]
        for line in lines:
            tb_item = line.find_all('td')
            if len(tb_item) >= 1:
                countries = tb_item[0].text.strip()
                quantity = tb_item[1].text.strip()
                value = tb_item[2].text.strip()
                if countries != "Total":
                    item = models.ImportationAndExportationDTO(year, countries, quantity, value)
                    data.append(item)

    return data
