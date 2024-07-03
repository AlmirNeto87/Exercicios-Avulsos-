print("Questao numero 1")
idade = int(input("Digite sua idade..!"))

if idade >=18:
    print("Voce e maior de idade")
else:
    print("Voce e menor de idade")

print()
print("Questao numero 2 ")
print()
print("Digite suas Notas para saber o Resultado ")
nota1 = int(input("Digite sua primeira nota "))
nota2 = int(input("Digite sua segunda nota "))

media = nota1+nota2/2

if media >=6:
    print(f"A media das suas nota foi",media)
    print("Voce esta aprovado")
else:
    print("Voce esta reprovado")

print()
print("Questao numero 3 ")
print()
print("Vamos calcular ua equacao de segunda grau")
a = float(input("digite o valor de a="))
b = float(input("digite o valor de b="))
c = float(input("digite o valor de c="))
delta = b**2-4*a*c
print("O valor de delta = ",delta)
raizdelta = delta**0.5
print("O Valor da raiz de delta = ",raizdelta)
x1=(-b+raizdelta)/(2*a)
print("Valor de x1 =",x1)
x2 =(-b-raizdelta)/(2*a)
print("Valor de x2 = ",x2)

print()
print("Questao numero 4 ")
print()

lista = [3,45,1]

lista.sort()
print(lista)

print()
print("Questao numero 5 ")
print()

print("Digite dois valores e tipo de operador ")
valor1 = int(input("Digite sua primeiro valor "))
valor2 = int(input("Digite sua segundo valor "))
operador = input(("Digite o operador "))

if  operador == "+":
    print("A soma dos dois valores =",valor1+valor2)
elif operador =="-":
    print("A subtracao dos dois valores =",valor1-valor2)
elif operador =="*":
    print("A multiplicacao dos dois valores =",valor1*valor2)
elif operador =="/":
    print("A divisao dos dois valores =",valor1/valor2)
else :
    print("Operador no reconhecido!")
