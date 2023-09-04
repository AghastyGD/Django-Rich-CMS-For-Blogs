# DJANGO RICH CMS FOR BLOGS (SISTEMA GERENCIADOR DE CONTEÚDOS COMPLETO PARA BLOGS)

Seja bem vindo a mais um meu projeto pessoal, este aqui é quase um código-aberto de como eu construí o CMS do meu site profissional: mozteek.com
Achei que poderia compartilhar algumas ideias bacanas que tive para implementar em CMS feito em Django, tornei fácil de manejar e mais completo possível. Optei pelo CKEditor como o nosso editor de texto (corpo da postagem) e a biblioteca autoslug com definação de algumas variáveis para gerar slugs automáticos e versatéis.

O objetivo do projeto é servir de ferramenta para blogueiros ou devs que pretendem um acesso rápido para construção e personalização de um CMS em Django e implementar em um site ou blog.

## INSTRUÇÕES DE USO

1 - pip install -r requirements.txt ( Instalar as dependências necessárias para o CMS funcionar)

2 - python manage.py createsuperuser ( Insira seu nome de usuario e senha desejada )

3 - python manage.py makemigrations / migrate ( Migração do Banco de Dados )

## EXECUÇÃO

1 - python manage.py runserver ( Iniciar o Servidor )


Para acessar o admin (Gerenciar Conteúdo), insira '/admin/' na url quando estive no navegador, por exemplo: 'http://127.0.0.1:8000/admin/'

O demo está rodando um template pronto baseado no site MozTeek apenas para demonstração, podes alterar para qualquer outro template ou criando da sua maneira! 

Isso é tudo! Espero ver você novamente em outro projeto empolgante hehehe! 

Qualquer dúvida contacte: https://aghastygd.pythonanywhere.com

