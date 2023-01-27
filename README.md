
# parse_cnab_file


## Descrição

Esse é um projeto que permite a conversão de um arquivo cnab simples por meio de requisições normais e upload de arquivos txt.

## Tabela de Conteúdos

- [Início Rápido](#início-rápido)
  - [Criação do ambiente virtual](#criação-do-ambiente-virtual)
  - [Entrando no ambiente virtual](#entrando-no-ambiente-virtual)
  - [Instalando dependências](#instalando-dependências)
  - [Rodando migrations](#rodando-migrations)
  - [Criando um superuser](#criando-um-superuser)
  - [Rodando o servidor](#rodando-o-servidor)
  - [Informações importantes](#informações-importantes)
  - [Upload de arquivo CNAB](#upload-de-arquivo-cnab)
  - [Gerando relatório](#gerando-relatório)


## Tecnologias Utilizadas
- Python
- Django
- Django Rest Framework
- Crispy forms

## Início Rápido

- ### Criação do ambiente virtual

```python
python -m venv venv
```

Se você está no windows, precisa permitir a criação do ambiente virtual
```bash
Set-ExecutionPolicy AllSigned
```


- ### Entrando no ambiente virtual

linux:
```
source venv/bin/activate
```

windows:
```
.\venv\Scripts\activate
```

<br>

- ### Instalando dependências

Esse comando instala recursivamente todas as dependências no arquivo requirements.txt

```python
pip install -r requirements.txt
```



- ### Rodando migrations

Isso vai criar as tabelas do banco de dados e popular a tabela de tipos com os valores default

```python
python manage.py migrate
```


- ### Rodando o servidor


```python
python manage.py runserver
```



- ### Informações importantes
  - Um arquivo chamado CNAB.txt é um exemplo de arquivo válido para upload que se encontra na base do projeto
  
  ###

- ### Upload de arquivo CNAB

Para fazer um upload de arquivo acesse a seguinte url:


```python
http://127.0.0.1:8000/api/report/ 

ou

http://localhost:8000/api/report/ 
```


Você irá fazer o upload do arquivo no formulário disponível, é obrigatório colocar um nome no momento de fazer o upload

- ### Gerando relatório
Só será necessário colocar o nome da loja que deseja ver as informações.

 ```python
http://127.0.0.1:8000/api/report/<nome da loja> 

ou

http://localhost:8000/api/report/MERCADO DA AVENIDA 
```

###

