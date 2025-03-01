# Sintaxe básica de programação em Python

# Imprimindo valores no console
print('Hello, World!')
print("Hello, World")
print("""\
Hello, 
    World!
""")

# Variáveis
nome = "Gabryel"
idade = 20
altura = 1.80

print(nome + "" " + idade + "" " + altura)

# Convertendo tipos de dados
idade = int(idade)
altura = float(altura)

# Operadores
num1, num2 = 4, 8

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2
div_inteira = num1 // num2
resto_divisao = num1 % num2
exponenciacao = num1 ** num2

# Recebendo valores do usuário
nome = input("Olá, qual o seu nome? : ")
idade = int(input("Qual a sua idade? : "))
altura = float(input("Qual a sua altura? : "))

# Interpolação de strings
print(f"Olá, {nome}. Prazer em te conhecer!")
print("Então você tem %d anos e %.2f de altura? Legal!" % (idade, altura))

comida_favorita_usuario = input("Qual sua comida favorita? : ")
comida_favorita_maquina = "Lasanha"

print("Você gosta de {1}? Que bacana, eu gosto de {0}.".format(comida_favorita_maquina, 
                                                                comida_favorita_usuario))
# Estruturas condicionais
print(f"Você tem {idade} né? Então você ", end="")
if idade < 16:
    print("ainda não pode votar.")
elif idade < 18 or idade > 70:
    print("tem voto opcional.")
else:
    print("tem voto obrigatório.")

# Listas e estruturas de repetição
lista_frases = ["Anotaram a data da maratona", "Pensar e repensar", "A base do teto desaba", "A cara rajada da jararaca"]

for frase in lista_frases:
    print(f"A frase \033[1m'{frase}'\033[m ", end="")
    frase_teste = frase.lower().replace(' ', '')
    if frase_teste == frase_teste[::-1]:
        print("é um palíndromo! A frase é a mesma lendo de trás para frente.")
    else:
        print("não é um palíndromo.")


# Dicionarios
contato = {"nome": "Gabryel", "email": "gabryel@email.com", "estado": "Goiás"}

for chave in contato:
    print(f"{chave}: {contato[chave]}")


# Funções
def calcular(operacao, num1, num2):
    def somar():
        return num1 + num2

    def subtrair():
        return num1 - num2

    def multiplicar():
        return num1 * num2

    def dividir():
        return num1 / num2

    match operacao:
        case "+":
            return somar()
        case "-":
            return subtrair()
        case "*":
            return multiplicar()
        case "/":
            return dividir()


print(calcular('*', 10, 10))
# Execute o código Python no terminal com python caminho_arquivo
