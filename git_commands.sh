# O Git clone é um comando para baixar o código-fonte existente de um repositório remoto (como o Github, por exemplo).
# Ex: https://github.com/marcusos/streamlit_app_tera.git
git clone <https://nome-do-link>

# O comando status do Git fornece todas as informações necessárias sobre o branch atual.
git status

# Precisamos usar o comando git add para incluir as alterações de um arquivo em nosso próximo commit (instancia de mudanças, um retrato do código).
# Ex: git add app.py
git add <nome_arquivo>

# Adiciona todos os arquivos modificados no próximo commit
git add .

# Este comando defini um ponto de verificação/retrato no processo de desenvolvimento, para o qual você pode voltar mais tarde, se necessário.
git commit -m "mensagem explicando a mudança no código"

# Enviar as alterações para o servidor remoto. OBS branch: Uma ramificação no git 
# EX: git push -u origin master
git push -u origin <nome-do-branch>

# O comando git pull é usado para obter atualizações do repositório remoto.
# Ex: git pull origin
git pull <remote>