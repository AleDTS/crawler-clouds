import click
import csv
import json
import os

from . import __version__
from . import vultr, digitalocean

crawlers = {
    "vultr": vultr,
    "digitalocean": digitalocean
}


def imprime(nome_crawler):
    crawler = crawlers[nome_crawler]
    for item in crawler.crawl():
        click.echo(item)


def salva_json(nome_crawler):
    crawler = crawlers[nome_crawler]

    arquivo = f'{nome_crawler}.json'
    itens = []

    for item in crawler.crawl():
        itens.append(item)

    if os.path.exists(arquivo):
        os.remove(arquivo)

    with open(arquivo, 'w') as f:
        f.write(json.dumps(itens))


def salva_csv(nome_crawler):
    crawler = crawlers[nome_crawler]

    arquivo = f'{nome_crawler}.csv'
    itens = []

    for item in crawler.crawl():
        itens.append(item)

    chaves = itens[0].keys()

    if os.path.exists(arquivo):
        os.remove(arquivo)

    with open(arquivo, 'w') as f:
        dw = csv.DictWriter(f, chaves)
        dw.writeheader()
        dw.writerows(itens)


@click.command()
@click.version_option(version=__version__)
@click.argument('crawler')
@click.option('--print', is_flag=True, help="Imprime resultados na tela")
@click.option('--save_json', is_flag=True, help="Salva dados em arquivo json")
@click.option('--save_csv', is_flag=True, help="Salva dados em arquivo csv")
def main(crawler, print, save_json, save_csv):
    """Crawler de informações para máquinas cloud"""
    if crawler not in ['vultr', 'digitalocean']:
        raise click.BadParameter("Argumento inválido")

    if print:
        imprime(crawler)

    if save_json:
        salva_json(crawler)

    if save_csv:
        salva_csv(crawler)
