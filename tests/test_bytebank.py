from codigo.bytebank import Funcionario

class TestClass:
    def test_quando_idade_recebe_03_02_200_deve_retornar_22(self):

        entrada = '03/02/1995' #Given
        esperado = 29

        funcionario_teste = Funcionario('Teste', entrada, 1111) #When
        resultado =  funcionario_teste.idade()

        assert resultado == esperado #Then