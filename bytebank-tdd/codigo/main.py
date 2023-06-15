from bytebank import Funcionario

#polly = Funcionario('Polly', '06/09/2001', 2000)
#print(polly.idade())

def teste_idade():
    funcionario_teste = Funcionario('Teste', '06/09/2001', 2000)
    print(f'Teste = {funcionario_teste.idade()}')
teste_idade()