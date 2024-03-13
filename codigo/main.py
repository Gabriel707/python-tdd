from codigo.bytebank import Funcionario


def teste_idade():
    funcionario_teste = Funcionario('Teste', '03/02/1995', 1111)
    print(f'Teste = {funcionario_teste.idade()}')

teste_idade()