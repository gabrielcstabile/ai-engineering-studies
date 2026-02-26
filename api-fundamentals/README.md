# API Fundamentals

Estudo sobre o funcionamento de APIs HTTP, com foco em compreender os conceitos por trás das requisições, protocolos e padrões arquiteturais — não apenas em como usá-los mecanicamente.

## Objetivos

- Entender como o protocolo HTTP funciona e por que ele é a base da comunicação na web
- Compreender a anatomia de uma requisição: métodos, headers, body, status codes
- Estudar o modelo REST e o que caracteriza uma API RESTful
- Trabalhar com autenticação (Basic Auth, Bearer Token, JWT)
- Consumir APIs reais e lidar com respostas, erros e paginação
- Ler e interpretar documentação de APIs

## Estrutura

```
labs/       # experimentos e scripts de estudo
```

## Tópicos Abordados

**HTTP e Requisições**
- Protocolo HTTP: verbos, headers, status codes
- Ciclo request/response
- Parâmetros de URL e query strings

**APIs REST**
- Princípios REST e o que diferencia uma API REST de outras abordagens
- Schemas de resposta e serialização JSON
- Composição de múltiplas APIs

**Autenticação**
- Basic Auth
- Bearer Token
- JSON Web Tokens (JWT)

**Ferramentas e Práticas**
- Biblioteca `requests` em Python
- Leitura de documentação (OpenAPI/Swagger)
- SDKs de terceiros vs. chamadas HTTP diretas

## Stack

- Python 3
- `uv` — gerenciamento de ambiente e dependências
- `requests`
- APIs públicas diversas (IBGE, OpenWeather, Spotify, entre outras)

## Setup

```bash
uv venv
source .venv/bin/activate
uv add requests
```

## Contexto

Este repositório faz parte de um conjunto de estudos em engenharia de dados e integração de sistemas. O foco está em entender os fundamentos antes de abstraí-los com frameworks ou SDKs de alto nível.
