# SonBlog - Desafio django (Construindo um Blog em minutos)

## Do que se trata?
Projetinho djando, com base em um [tutorial](https://www.youtube.com/watch?v=eK2sfDWQUXc) do Canal [School of Net](https://www.youtube.com/channel/UCIlafifr-E57jct9knCrZzw), no Youtube.

O projeto é basicamente...

## Este projeto foi feito com:
- Python 3.8.2
- pip 20.1
- Django 3.0.6
- django-cheditor
- django-js-asset
- Pillow

## Como rodar o projeto?
1. Clone esse repositório.
    ```
    1. git clone https://github.com/RamonAlves1357/SonBlog/
    2. cd SonBlog
    ```
2. Crie um virtualenv com Python 3.
    ```
    3. python3 -m venv .venv
    ```
3. Ative o virtualenv.
    - No linux ou MacOS: 
        ```
        4. source .venv/bin/activate
        ```
    - No Windows:
        ```
        4. .venv\scripts\activate
        ```

4. Instale as dependências.
    ```
    5. pip install --upgrade pip
    6. pip install django
    7. pip install -r requirements.txt
    8. python contrib/env_gen.py
    ```

5. Rode as migrações.
    ```
    9. python manage.py migrate
    10. python manage.py createsuperuser
    11. python manage.py runserver
    ```
