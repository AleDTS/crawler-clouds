import requests
import lxml.html


def conteudo_2_arvore(url: str):
    r = requests.get(url)
    arvore = lxml.html.fromstring(r.content)
    return arvore
