import requests
import lxml.html


def traz_conteudo(url: str):
    r = requests.get(url)
    return r.content


def pega_arvore(html: str):
    arvore = lxml.html.fromstring(html)
    return arvore