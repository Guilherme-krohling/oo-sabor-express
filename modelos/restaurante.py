from modelos.avaliacao import Avaliacao

class Restaurante():
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
        
    def __str__(self):
        return f'{self._nome}, {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'nome'.ljust(15)} | {'categoria'.ljust(15)} | {'Avaliacao'.ljust(25)} | {'status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(15)} | {restaurante._categoria.ljust(15)} | {str(restaurante.media_avaliacao).ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return 'ativado' if self._ativo else 'desativado'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if nota > 5 or nota < 0:
            raise ValueError('Nota deve ser entre 0 e 10')
        else:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacao(self):
        if not self._avaliacao:
            return 'Restaurante sem avaliação'
        soma = sum(avaliacao._nota for avaliacao in self._avaliacao)
        return round(soma / len(self._avaliacao),1)













# restaurante_praca.nome= 'Praça'
# restaurante_praca.categoria = 'Gourmet'

# print(f'Nome: {restaurante_praca.nome},\nCategotia: {restaurante_praca.categoria}\n')

# #01.CLASSES AULA 7
# restaurante_praca.categoria = 'Italiana'
# nome_do_restaurante= restaurante_praca.nome

# if restaurante_praca.ativo:
#     print("Restaurante está ativo !!\n")
# else:
#     print('Restaurante está inativo\n')

# categoria= Restaurante.categoria
# restaurante_praca.nome='Bistrô'
# #----------------

# restaurante_pizza = Restaurante('Pizza', 'Fast Food')
# restaurante_pizza.nome='Pizza place'
# restaurante_pizza.categoria='Fast Food'

# if restaurante_pizza.categoria == 'Fast Food\n':
#     print('A categoria é Fast Food !!')
# else:
#     print('A categoria não é Fast Food\n')

# restaurante_pizza.ativo=True

# restaurantes = [ restaurante_praca, restaurante_pizza]

# print(restaurantes)