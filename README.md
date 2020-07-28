Web crawler que captura informações de provedores de computação em nuvem.

## Sobre

### Provedores

-   [Digital Ocean](https://www.digitalocean.com/pricing/#droplet)
-   [Vultr](https://www.vultr.com/products/cloud-compute/)

### Dados Capturados

-   CPU / VCPU
-   MEMORY
-   STORAGE / SSD DISK
-   BANDWIDTH / TRANSFER
-   PRICE [ $/mo ]

## Pré requisitos

-   [Poetry](https://github.com/python-poetry/poetry#installation)

## Instalação

```sh
poetry install
```

## Uso

1. Entrar no ambiente virtual ou executar comandos com `poetry run`

```sh
poetry shell
```

2. Verificar instalação do pacote

```sh
crawler-clouds --version
```

3. Para executar:

```sh
crawler-clouds [OPCOES] CRAWLER
```

### Opções

-   --print

    Imprime resultados na tela

-   --save_json

    Salva dados em arquivo json

-   --save_csv

    Salva dados em arquivo csv

## A Fazer

-   Tratar e normalizar dados
