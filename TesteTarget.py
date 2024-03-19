'''Primeiro Teste'''
indice = 13
soma = 0
k = 0
while k < indice:
    k = k + 1
    soma = soma + k

print("O resultado é:", soma)
'''Ao final do laço de repetição do while o valor da variavel da soma é 91'''

'''Segundo teste'''
def fibo(n):
    a = 0
    b = 1
    while b < n:
        temporario = a
        a = b
        b = temporario + b
    if b == n:
        return f"{n} pertence à sequência de Fibonacci."
    else:
        return f"{n} não pertence à sequência de Fibonacci."


numero_para_verificar = eval(input("Digite um número: "))
print(fibo(numero_para_verificar))

'''Quinto desafio'''
def inverter(x):
  string = ''
  for i in x:
      string = i + string
  return string


print(inverter(str(input("Digite um texto para ser invertido: "))))

