import pytest
from codigo.bytebank import Funcionario
from pytest import mark

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
    

    def test_quando_funcionario_recebe_1000_deve_receber_bonus_10_porcentos(self):
        entrada_minima = 1000
        #entrada_maxima = 10000
        #entrada_q_nao_consedera_bonus = 10001
        esperado = 1100

        funcionario_teste_minimo = Funcionario('teste minimo', '11/11/2000', entrada_minima)
        #funcionario_teste_maximo = Funcionario('teste maximo', '11/11/2000', entrada_maxima)
        
        #funcionario_teste_maximo.calcular_bonus()
        funcionario_teste_minimo.calcular_bonus()
        resultado = funcionario_teste_minimo.salario
        #resultado = funcionario_teste_maximo.salario

        assert resultado == esperado


    def test_quando_funcionario_recebe_10000_retornar_exeption(self):
        with pytest.raises(Exception):
            entrada = 10000  # given

            funconario_teste = Funcionario('teste', '11/11/2000', entrada)
            resultado = funconario_teste.calcular_bonus()  # when

            assert resultado  # then

    def test_retorno_str(self):
        nome, data_nascimento, salario = 'Polly', '12/03/2000', 1000# Given
        esperado = 'Funcionario(Polly, 12/03/2000, 1000)'

        pollyana = Funcionario(nome, data_nascimento, salario)
        resultado = pollyana.__str__() #When

        assert resultado == esperado

    def test_retornar_salario_igual_a_1500_retornar_1350_depois_de_descontado_fgts_de_10_porcentos(self):
        salario = 1500
        esperado = 1350

        funcionario_teste = Funcionario('teste', '11/11/2001', salario)

        resultado = funcionario_teste.desconto_fgts()

        assert resultado == esperado

    def test_retornar_somente_salario_quando_salario_for_menor_ou_igual_ha_1300(self):
        salario = 1300
        esperado = 1300

        funcionario_teste = Funcionario('teste', '11/11/2001', salario)

        resultado = funcionario_teste.desconto_fgts()

        assert resultado == esperado