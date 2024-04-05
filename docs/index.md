### Tutorial: Implementando Cache Simples em uma Aplicação Flask

Neste tutorial, vamos criar uma aplicação Flask simples que simula a recuperação de questões paginadas de um banco de dados e utiliza um cache simples para armazenar os resultados e melhorar o desempenho.

#### Passo 1: Configuração do Ambiente

Certifique-se de ter o Python e o Flask instalados. Se necessário, instale o Flask com o seguinte comando:

```bash
pip install Flask
```

#### Passo 2: Criação da Aplicação Flask

Crie um arquivo chamado `src/main.py` e adicione o seguinte código:

```python
from flask import Flask, request
import time

main = Flask(__name__)

conteudo_mock = [
    {'questao': 1, 'texto': 'etc etc etc etc etc'},
    {'questao': 2, 'texto': 'etc etc etc etc etc'},
    {'questao': 3, 'texto': 'etc etc etc etc etc'}
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
        time.sleep(.5)  # Simula um atraso
        salva_cache_simulado(chave_cache, conteudo_mock)
        conteudo_do_cache_simulado = conteudo_mock
    else:
        conteudo_do_cache_simulado = conteudo_do_cache_simulado.get('dados')

    return conteudo_do_cache_simulado

def resgata_cache_simulado(chave):
    return obj.get(chave)

def salva_cache_simulado(chave, conteudo):
    obj[chave] = {"dados": conteudo, "tempo_limite": time.time()}

if __name__ == "__main__":
    main.run(port=5000)
```

#### Passo 3: Entendendo o Código

- A aplicação Flask possui um único endpoint (`/`) que aceita parâmetros de consulta `pagina` e `qtd-por-pagina` para simular a recuperação paginada de questões.
- A função `resgata_questoes` verifica se os dados já estão no cache (simulado pelo dicionário `obj`). Se os dados não estiverem no cache ou se o tempo limite de 5 segundos tiver sido excedido, a função simula um atraso (para representar o tempo de acesso a um banco de dados) e salva os dados mock no cache.
- As funções `resgata_cache_simulado` e `salva_cache_simulado` são utilizadas para interagir com o cache.

#### Passo 4: Executando a Aplicação

Execute a aplicação com o seguinte comando:

```bash
python src/main.py
```

A aplicação estará rodando no endereço `http://localhost:5000`. Você pode testar o endpoint acessando URLs como `http://localhost:5000/?pagina=1&qtd-por-pagina=2` em seu navegador ou utilizando ferramentas como cURL ou Postman.

#### Contribuições

Henrique Higa - RA: 10390109
<br/>
Implementação da API, implementação do CACHE em memória e criação da documentação.