class Pessoa:
    nome = ''
    telefone = ''

    def imprimir(self):
        print("Nome: {0}, Telefone: {1}".format(self.nome, self.telefone))


p1 = Pessoa()
p1.nome = 'Maria'
p1.telefone = '3232-1212'

p2 = Pessoa()
p2.nome = 'Jose'
p2.telefone = '3434-2323'

Pessoa.nome = 'Antonio'

p1.imprimir()
p2.imprimir()
print(Pessoa.nome)