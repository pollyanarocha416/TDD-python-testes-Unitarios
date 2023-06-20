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

    def test_quando_sobre_nome_recebe_Pollyana_Rocha_deve_retornar_Rocha(self):
        entrada = ' Pollyana Rocha '# Given
        esperado = 'Rocha'

        pollyana = Funcionario(entrada, '06/09/2001', 2000)
        resultado = pollyana.sobrenome() #When

        assert resultado == esperado


    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        #given
        entrada_salario = 100000
        entrada_nome = 'Paulo Bragança'
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, '11/11/2000', entrada_salario)
        #when
        funcionario_teste.decrescimo_salario()
        resultado = funcionario_teste.salario

        #then
        assert resultado == esperado
   