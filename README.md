# Loja de Instrumentos - Projeto Acadêmico

Este é um projeto acadêmico desenvolvido com o framework Django, utilizando a arquitetura MVT (Model-View-Template). O objetivo do projeto é criar uma aplicação web para gerenciar uma loja de instrumentos musicais, incluindo funcionalidades administrativas e de gerenciamento de produtos.

## Arquitetura do Projeto

O projeto segue a arquitetura MVT (Model-View-Template):

- Model (Modelo): Representa as tabelas do banco de dados e gerencia as interações com os dados.
- View (Visão): Controla a lógica de negócios e conecta os modelos às templates.
- Template (Template): Responsável pela interface do usuário e pela exibição dos dados no navegador.

## Diagrama Entidade-Relacionamento

O projeto foi modelado com base no seguinte diagrama entidade-relacionamento (ER):

![Diagrama ER do Banco de Dados](/ProgWeb_ER_Diagram_GuitarStore.drawio.png)

## Funcionalidades Atuais

- Modelagem completa do banco de dados:
    - Produto: Gerencia informações gerais de produtos.
    - Instrumentos: Inclui instrumentos de corda, sopro e percussão, cada um com suas especificidades.
    - Pedido: Relaciona usuários a produtos e calcula valores totais.
- Tela de administração padrão do Django para gerenciar os dados.

## Requisitos Técnicos

- Linguagem: Python 3.8.1
- Framework: Django 5.1.4
- Banco de Dados: SQLite
- Frontend: Utiliza o template padrão do Django (ainda sem estilização adicional).

## Como Executar o Projeto

Clone o repositório:
``` bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```
Acesse o diretório do projeto:
``` bash
cd nome-do-projeto
```
Crie e ative um ambiente virtual:
``` bash
python3 -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```
Instale as dependências:
``` bash
pip install -r requirements.txt
```
Realize as migrações do banco de dados:
``` bash
python manage.py migrate
```
Crie um superusuário para acessar o painel administrativo:
``` bash
python manage.py createsuperuser
```
Inicie o servidor de desenvolvimento:
``` bash
python manage.py runserver
```
Acesse o sistema no navegador em: http://127.0.0.1:8000/admin

## Próximos Passos

- Criar templates para as páginas de usuário.
- Implementar estilização com Bootstrap.
- Adicionar autenticação para usuários.
- Desenvolver funcionalidades de carrinho de compras.