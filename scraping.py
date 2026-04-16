import requests
from bs4 import BeautifulSoup


def buscar_noticias():
    # URL do portal de notícias
    url = "https://g1.globo.com/"


    # 1. Faz a requisição HTTP para obter o conteúdo da página
    response = requests.get(url)
    response.raise_for_status()  # Verifica se houve erro na requisição

    # 2. Transforma o HTML em um objeto BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # 3. Localiza os itens de notícia (no G1, geralmente ficam em classes 'feed-post-body')
    noticias = soup.find_all('div', class_='feed-post-body')

    print(f"--- Últimas Notícias do G1 ({len(noticias)} encontradas) ---\n")

    for i, noticia in enumerate(noticias, 1):
        # Extraindo o título e o link (tag <a> dentro da classe 'feed-post-link')
        manchete = noticia.find('a', class_='feed-post-link')

        if manchete:
            titulo = manchete.text.strip()
            link = manchete['href']

            # Extraindo o resumo/descrição (opcional)
            resumo = noticia.find('div', class_='feed-post-body-resumo')
            descricao = resumo.text.strip() if resumo else "Sem descrição disponível."

            print(f"{i}. {titulo}")
            print(f"   Link: {link}")
            print(f"   Resumo: {descricao}")
            print("-" * 50)


if __name__ == "__main__":
    buscar_noticias()