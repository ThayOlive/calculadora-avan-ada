Olá! 
Foi um prazer realizar este teste.

Passo a apsso para executar essa Calculadora Avançada 

1. Crie um ambinente virtual, no terminal:
python -m virtualenv nome-do-ambiente-virtual (ex: venv)

2. Ative o ambinete virtual:
nome-do-ambiente-virtual\scripts\activate

3. Instale as bibliotecas utilizadas:
pip install -r requirements.txt

4. Rode as migrações:
python manage.py makemigrations 
python manage.py migrate

5. Crie um superusuario:
 python manage.py createsuperuser

6. Rode o servidor:
python manage.py runserver

7. Acesse o admin do Django:
(http://localhost:8000/admin)

8. Crie um usuario em:
Usuarios > + Adcionar

9. Acesse a url principal e logue com o usuario criado:
(http://localhost:8000/)

Agora é só começar a fazer os calculos!

Sugestão para visualização mais simplificada dos usuarios no banco de dados (conforme o diagrama pedido), executar uma query na tabela calc_app_usuario:

SELECT id, first_name, username, password, dt_inclusao FROM calc_app_usuario LIMIT 100


Obrigada. 

