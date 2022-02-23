from pessoa import  Pessoa

p1 = Pessoa('Luiz',29)
p2 = Pessoa ('João', 32)

p1.comer('pizza')
p2.falar('sexo')
p1.pararComer()
print(p1.getAnoNascimento())
print(p2.getAnoNascimento())