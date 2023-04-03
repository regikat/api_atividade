from models import Pessoas, Usuarios

#Insere dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Joaquim', idade=30)
    print(pessoa)
    pessoa.save()

#Consulta dados da tabela pessoa
def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='Joao').first()   #consulta Pessoas filtrando pelo joão 1 ocorrencia
    print(pessoa.nome,pessoa.idade)                         #printa nome e idade

#Altera dados na tabela Pessoa
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Reginaldo').first()
    pessoa.nome = 'Ramiro'
    pessoa.save()

#Exclui registro da tabela Pessoa
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Joao').first()
    pessoa.delete()

def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)

if __name__ == '__main__':
   insere_usuario('Reginaldo', '1234')
   insere_usuario('Sofia', '4321')
   consulta_todos_usuarios()
   # insere_pessoas()
   # altera_pessoa()
   # exclui_pessoa()
   #consulta_pessoas()
