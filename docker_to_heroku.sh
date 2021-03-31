# Acesso a sua conta Heroku
heroku login

# Acesso ao Container Registry ou repositório de imagens
heroku container:login

# Atribuir a imagem criada ao padrão do Container Registry do heroku
# ex: docker tag streamlit-tera registry.heroku.com/ds-streamlit-tera/web
docker tag [NOME DA IMAGEM] registry.heroku.com/[NOME DO APP]/web

# Carregar a imagem e criar o container
# ex: docker push registry.heroku.com/ds-streamlit-tera/web
docker push registry.heroku.com/[NOME DO APP]/web

# Aprovar as alterações
# ex: heroku container:release web --app ds-streamlit-tera
heroku container:release web --app [NOME DO APP]

# Hora da verdade: abrir o aplicativo no navegador
# ex: heroku open --app ds-streamlit-tera
heroku open --app [NOME DO APP]

# OUTROS COMANDOS

# Deletar a imagem local criada para ser enviada ao reistry do heroku
docker rmi --f registry.heroku.com/[NOME DO APP]/web

# Verificar o log da aplicação no heroku
heroku logs --tail