from codigo.bytebank import Funcionario


def teste_idade():
    funcionario_teste = Funcionario('Teste', '03/02/2000', 1111)
    print(f'Teste = {funcionario_teste.idade()}')

    funcionario_teste = Funcionario('Teste', '03/02/1999', 1111)
    print(f'Teste = {funcionario_teste.idade()}')

    funcionario_teste = Funcionario('Teste', '03/12/1995', 1111)
    print(f'Teste = {funcionario_teste.idade()}')

teste_idade()