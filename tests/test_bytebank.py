from codigo.bytebank import Funcionario

class TestClass:
    def test_quando_idade_recebe_03_02_200_deve_retornar_22(self):

        entrada = '03/02/1995' #Given
        esperado = 29

        funcionario_teste = Funcionario('Teste', entrada, 1111) #When
        resultado =  funcionario_teste.idade()

        assert resultado == esperado #Then

    def test_quando_sobrenome_recebe_Gabriel_Araujo_deve_retornar_apenas_Araujo(self):
        entrada = ' Gabriel Araujo ' # Given
        esperado = 'Araujo'

        gabriel = Funcionario(entrada, '03/02/1995', 1111)
        resultado = gabriel.sobrenome()

        assert resultado == esperado