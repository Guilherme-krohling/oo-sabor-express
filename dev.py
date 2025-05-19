from modelos.restaurante import Restaurante

restaurante_pf = Restaurante('Pratin', 'prato feito')
restaurante_mex = Restaurante('Mexicano', 'comida mexicana')
restaurante_mc = Restaurante('Mc', 'fast food')

restaurante_mex.alternar_estado()

restaurante_pf.receber_avaliacao('GUI', 5)
restaurante_pf.receber_avaliacao('Dani', 5)
restaurante_pf.receber_avaliacao('Mari', 5)
restaurante_pf.receber_avaliacao('Cello', 5)



def main():
    Restaurante.listar_restaurantes()

if __name__ == "__main__":
    main()