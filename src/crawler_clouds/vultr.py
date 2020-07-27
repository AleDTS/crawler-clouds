from .base import conteudo_2_arvore
from lxml import etree


URL = "https://www.vultr.com/products/cloud-compute/"

XPATH_LINHAS = "//div[@id='compute']//div[@data-row]"
XPATH_COLUNA = "./div[$col]//text()"


def crawl():

    arvore = conteudo_2_arvore(URL)

    txts_col = etree.XPath(XPATH_COLUNA)

    for div in arvore.xpath(XPATH_LINHAS):

        yield {
            "cpu": txts_col(div, col=3)[2],
            "mem": txts_col(div, col=4)[1],
            "sto": txts_col(div, col=2)[2],
            "band": txts_col(div, col=5)[2],
            "price": txts_col(div, col=6)[2]
        }
