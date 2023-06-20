from datetime import date

class Funcionario:
    def __init__(self, nome, data_nascimento, salario) -> None:
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._salario = salario

    @property
    def nome(self):
        return self._nome
    
    @property
    def salario(self):
        return self._salario
    
    def idade(self):
        data_nascimento = self._data_nascimento.split('/')
        ano_nascimento = data_nascimento[-1]
        ano_atual = date.today().year

        return ano_atual - int(ano_nascimento)

    def sobrenome(self):
        nome_completo = self.nome.strip()
        nome_quebrado = nome_completo.split(' ')
        return nome_quebrado[-1]

    def calcular_bonus(self):
        valor = self._salario * 0.1
        if valor > 1000:
            valor = 0
        return valor

    def __str__(self):
        return f'Funcionario({self._nome}, {self._data_nascimento}, {self._salario})'
    

    def decrescimo_salario(self):
        sobrenomes = ['Bragança', 'Windsor', 'Bourbon', 'Yamato', 'Al Saud', 'Khan', 'Tudor', 'Ptolomeu']
        # prof solução
        if self._salario >= 100000 and (self.sobrenome() in sobrenomes):
            decrescimo = self._salario * 0.1
            self._salario -= decrescimo
        
        # minha solução
        #if self._salario >= 100000 and (self.sobrenome() in sobrenomes):
        #    desconto_salarial =  self._salario * 0.1
        #    decrescimo_salario = self._salario - desconto_salarial
        #    self._salario = decrescimo_salario
        #return decrescimo