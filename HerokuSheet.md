# Logar no servidor do app:

    	heroku login

# Logar com credenciais no terminal:

	heroku login -i

# Conectar com git:

   	heroku git:remote -a siteName

# Usar Git para clonar repositório Heroku para máquina local:

	heroku git:clone -a app_name

	cd \app_name

# Subir mudanças:

	git push heroku main

# Verificar log de atividades:

   	heroku logs --tail
    
# Criar super user em app:

  	heroku run python manage.py createsuper user

# Migrar mudanças nos models.py:

	heroku run python manage.py migrate


