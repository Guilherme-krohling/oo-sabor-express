# class Musica:
#     def __init__(self, nome='', artista='', duracao=0):
#         self.nome = nome
#         self.artista = artista
#         self.duracao = duracao


# musica1 = Musica(nome='Under Pressure', artista='Queen & David Bowie', duracao=248)
# musica2 = Musica(nome='The Trooper', artista='Iron Maiden', duracao=245)
# musica3 = Musica(nome='Hotel California', artista='Eagles', duracao=390)

# class Pessoa:
#     def __init__(self, nome='', idade=0, profissao=''):
#         self.nome = nome
#         self.idade = idade
#         self.profissao = profissao

#     def __str__(self):
#         return f'Nome: {self.nome}, Idade: {self.idade}, Profissão: {self.profissao}'
        
#     def aniversario(self):
#         self.idade += 1

#     @property
#     def saudacao(self):
#         print(f'Olá, meu nome é {self.nome} e eu tenho {self.idade} anos. Sou {self.profissao}.')
    

# pessoa1 = Pessoa(nome='João', idade=30, profissao='Engenheiro')	
# print(pessoa1)
# pessoa1.aniversario()
# print(pessoa1)
# pessoa1.saudacao

# class ContaBancaria:
#     def __init__(self, titular, saldo):
#         self.titular = titular
#         self.saldo = saldo
#         self._ativo=False

#     def __str__(self):
#         return f'Titular: {self.titular}, Saldo: {self.saldo}, Ativo: {self._ativo}'
    
#     def ativar_conta(self):
#         self._ativo=True

# conta1 = ContaBancaria('João', 1000)
# conta2 = ContaBancaria('Maria', 2000)
# print(conta1)
# print(conta2)

# conta1.ativar_conta()
# print(conta1)


# class ClienteBanco:
#     clientes = []

#     def __init__(self, nome, idade, profissao, cpf, endereco):
#         self.nome = nome
#         self.idade = idade
#         self.profissao = profissao
#         self.cpf = cpf
#         self.endereco = endereco
#         ClienteBanco.clientes.append(self)

#     @classmethod
#     def listar_clientes(cls):
#         print(f'{"Nome"} | {"Idade"} | {"Profissão"} | {"Limite"} | {"Ativo"}')
#         for cliente in cls.clientes:
#             print(f'{cliente.nome} | {cliente.idade} | {cliente.profissao} | {cliente.cpf} | {cliente.endereco}')



# cliente1 = ClienteBanco('João', 30, 'Engenheiro', '123.456.789-00', 'Rua A, 123')
# cliente2 = ClienteBanco('Maria', 25, 'Médica', '987.654.321-00', 'Rua B, 456')
# cliente3 = ClienteBanco('Pedro', 40, 'Professor', '456.789.123-00', 'Rua C, 789')
# cliente4 = ClienteBanco('Ana', 35, 'Arquiteta', '321.654.987-00', 'Rua D, 101')

# ClienteBanco.listar_clientes()

