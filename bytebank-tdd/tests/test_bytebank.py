from codigo.bytebank import Funcionario


class TestClass:
    def test_quando_idade_recebe_06_09_2001_retornar_22(self):
        # Given - Contexto
        entrada = '06/09/2001'
        esperado = 22
        funcionario_teste = Funcionario('Polly', entrada, 2000)
        
        # When - Ação
        resultado = funcionario_teste.idade()
        
        # Then - Desfecho
        assert resultado == esperado

        pass