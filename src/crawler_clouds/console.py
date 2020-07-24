import click

from . import __version__
from . import vultr

crawlers = {
    "vultr": vultr,
}


def imprime(nome_crawler):
    crawler = crawlers[nome_crawler]
    for item in crawler.crawl():
        click.echo(item)


@click.command()
@click.version_option(version=__version__)
@click.argument('crawler')
@click.option('--print', is_flag=True, help="Imprime resultados na tela")
def main(crawler, print):
    """Crawler de informações para máquinas cloud"""
    if crawler not in ['vultr']:
        raise click.BadParameter("Argumento inválido")

    if print:
        imprime(crawler)
