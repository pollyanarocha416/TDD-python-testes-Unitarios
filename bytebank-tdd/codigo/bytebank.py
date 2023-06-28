from datetime import date


class Funcionario:
    def __init__(self, nome, data_nascimento, salario) -> None:
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._salario = salario

    @property
    def nome(self) -> str:
        return self._nome
    
    @property
    def salario(self) -> float:
        return self._salario
    
    def idade(self) -> float:
        data_nascimento = self._data_nascimento.split('/')
        ano_nascimento = data_nascimento[-1]
        ano_atual = date.today().year

        return ano_atual - int(ano_nascimento)

    def sobrenome(self) -> str:
        nome_completo = self.nome.strip()
        nome_quebrado = nome_completo.split(' ')
        
        return nome_quebrado[-1]

    def calcular_bonus(self) -> float:
        if self._salario >= 1000 and self._salario <= 10000:
            valor = self._salario * 0.1
            self._salario += valor
    
    def __str__(self) -> str:
        
        return f'Funcionario({self._nome}, {self._data_nascimento}, {self._salario})'
    
    def _diretor(self) -> float:
        sobrenomes = ['Bragança', 'Windsor', 'Bourbon', 'Yamato', 'Al Saud', 'Khan', 'Tudor', 'Ptolomeu']
        
        return self._salario >= 100000 and (self.sobrenome() in sobrenomes)      

    def decrescimo_salario(self) -> float:
        if self._diretor():
            decrescimo = self._salario * 0.1
            self._salario -= decrescimo
