from .base import conteudo_2_arvore
from lxml import etree


URL = "https://www.digitalocean.com/pricing/#droplet"

XPATH_LINHAS = "//section[.//div[@id='standard-droplets']]//tbody//tr"
XPATH_COLUNA = "./td[$col]/text()"


def crawl():

    arvore = conteudo_2_arvore(URL)

    txt_col = etree.XPath(XPATH_COLUNA)

    for tr in arvore.xpath(XPATH_LINHAS):

        yield {
            "cpu": txt_col(tr, col=2)[0],
            "mem": txt_col(tr, col=1)[0],
            "sto": txt_col(tr, col=4)[0],
            "band": txt_col(tr, col=3)[0],
            "price": txt_col(tr, col=6)[0]
        }
