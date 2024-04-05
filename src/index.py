import json
from flask import Flask, request
import time

main = Flask(__name__)

conteudo_mock = [
    {
        'questao': 1,
        'texto': 'etc etc etc etc etc'
    },
    {
        'questao': 2,
        'texto': 'etc etc etc etc etc'
    },
    {
        'questao': 3,
        'texto': 'etc etc etc etc etc'
    }
]

obj = {}


@main.route("/")
def resgata_questoes_por_pagina_e_qtd_por_pagina():
    pagina = request.args.get('pagina')
    qtdPorPagina = request.args.get('qtd-por-pagina')
    return resgata_questoes(pagina, qtdPorPagina)


def resgata_questoes(pagina, qtdPorPagina):
    chave_cache = f'pagina-{pagina}-qtd-por-pagina-{qtdPorPagina}'
    conteudo_do_cache_simulado = resgata_cache_simulado(chave_cache)

    if conteudo_do_cache_simulado is None or time.time() - conteudo_do_cache_simulado.get("tempo_limite") > 5:
        time.sleep(.5)
        salva_cache_simulado(chave_cache, conteudo_mock)
        conteudo_do_cache_simulado = conteudo_mock
    else:
        conteudo_do_cache_simulado = conteudo_do_cache_simulado.get('dados')

    return conteudo_do_cache_simulado


def resgata_cache_simulado(chave):
    return obj.get(chave)


def salva_cache_simulado(chave, conteudo):
    obj[chave] = {
        "dados": conteudo,
        "tempo_limite": time.time()
    }


main.run(port=5000)
