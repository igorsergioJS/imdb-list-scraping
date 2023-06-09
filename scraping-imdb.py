import requests
import json
import csv
from bs4 import BeautifulSoup

# URL base da lista de filmes

link_list = "https://www.imdb.com/list/ls556047343"

base_url = link_list + "/?st_dt=&mode=detail&page="

# Número de páginas a serem obtidas
num_paginas = 1

# Lista para armazenar as informações dos filmes
informacoes_filmes = []

for pagina in range(1, num_paginas+1):
    url = base_url + str(pagina) + "&sort=list_order,asc"

    # Fazendo a requisição HTTP para a página
    response = requests.get(url)

    # Criando um objeto BeautifulSoup com o conteúdo da página
    soup = BeautifulSoup(response.text, "html.parser")

    # Encontrando todos os elementos <div> que contenham a classe "lister-item mode-detail"
    filmes = soup.find_all("div", class_="lister-item mode-detail")

    # Iterando sobre os elementos encontrados e extraindo as informações dos filmes
    for filme in filmes:
        # Extraindo o elemento âncora que contém o nome do filme
        movie_name_anchor = filme.find("h3", class_="lister-item-header").find("a")

        # Extraindo o ID do filme a partir do atributo href
        movie_id = movie_name_anchor["href"].split("/")[2]

        # Extraindo o nome do filme
        movie_name = movie_name_anchor.text

        # Extraindo o ano de lançamento do filme
        year = filme.find("span", class_="lister-item-year").text.strip("()")

        # Extraindo o tempo de duração do filme
        runtime = filme.find("span", class_="runtime").text.strip()

        # Extraindo a classificação indicativa do filme
        certificate_element = filme.find("span", class_="certificate")
        certificate = certificate_element.text.strip() if certificate_element else ""

        # Extraindo o link da imagem do poster do filme
        poster_img = filme.find("img", class_="loadlate")
        poster_link = poster_img["loadlate"] if poster_img else ""

        # Extraindo o metascore do filme
        metascore_element = filme.find("span", class_="metascore")
        metascore = metascore_element.text.strip() if metascore_element else ""

        # Extraindo nome dos atores e diretores
        elements = filme.find_all("p")[2].find_all("a")
        directors = []
        stars = []
        current_role = None
        for element in elements:
            text = element.previous_sibling.strip()
            if text == "Director:" or text == "Directors:":
                current_role = "director"
            elif text == "Stars:":
                current_role = "star"

            if current_role == "director":
                directors.append(element.text.strip())
            elif current_role == "star":
                stars.append(element.text.strip())

        # Extraindo a arrecadação do filme
        gross_element = filme.find("span", class_="text-muted text-small")
        gross = gross_element.text.strip().split(":")[1].strip() if gross_element else ""

        # Extraindo os principais gêneros do filme
        genres_elements = filme.find("span", class_="genre").find_all("a")
        genres = [genre.text.strip() for genre in genres_elements]

        # Extraindo a nota do IMDB
        imdb_rating = filme.find("div", class_="ipl-rating-star small").find("span", class_="ipl-rating-star__rating").text.strip()

        # Criando um dicionário com as informações do filme
        filme_info = {
            "name": movie_name,
            "id": movie_id,
            "year": year,
            "runtime": runtime,
            "certificate": certificate,
            "poster_link": poster_link,
            "metascore": metascore,
            "directors": directors,
            "stars": stars,
            "gross": gross,
            "genres": genres,
            "imdb_rating": imdb_rating
        }

        informacoes_filmes.append(filme_info)

# Salvando as informações dos filmes em um arquivo JSON
with open("ex_file.json", "w", encoding="utf-8") as json_file:
    json.dump(informacoes_filmes, json_file, indent=4, ensure_ascii=False)

# Salvando as informações dos filmes em um arquivo CSV
csv_headers = ["name", "id", "year", "runtime", "certificate", "poster_link", "metascore", "director", "stars", "gross", "genres", "imdb_rating"]
csv_data = [list(filme.values()) for filme in informacoes_filmes]

with open("ex_file.csv", "w", newline="", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(csv_headers)
    writer.writerows(csv_data)

print("Arquivos salvos com sucesso: filmes.json e filmes.csv")
