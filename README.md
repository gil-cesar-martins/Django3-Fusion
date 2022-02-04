# Django3-Fusion

Aplicativo onde uma equipe de desenvolvedores pode prestar diversos serviços aos clientes.

### Deploy local 
Instale as dependências no <b>requirements.txt<b>:
 
`pip install -r requirements.txt`
 
 Exporte um ENVIRONMENT para definir o banco de dados para o teste
 
 `export ENVIRONMENT == 'test'`
 
 Qualquer alteração nos **models** deve ser concluída com o comando:
 
 `python manage.py makemigrations`
 
 E depois migrar os **models** para o banco de dados:
 
 `python manage.py migrate`
 
 Crie um superusuário para o gerenciamento do banco de dados:
 
 `python manage.py createsuperuser`
 
 Execute sua aplicação:
 
 `python manage.py runserver`
 
 Para acessar vá no seu navegador e  digite [http://localhost:8000](http://localhost:8000)



