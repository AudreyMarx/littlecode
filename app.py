# Experimento Científico - 3°L
# Alunos: Audrey Marques e Jackson de alguma coisa
# Calculadora IMC + índice de ingestão de água

nome = input("Olá! Seja bem vindo(a). Qual o seu nome? ")
idade = input("É bom te ver por aqui {}. Qual sua idade? ".format(nome))
peso = float(input("E qual seu peso? (Kg) "))
altura = float(input("Qual sua altura? "))

imc = peso / (altura ** 2) #var de calculo do Índice de Massa Corporal (IMC)
agua_dia = (peso * 35) #var do calculo de consumo diário de água para adultos entre 18 e 55 anos

print("\n{}, você está com: {} anos".format(nome, idade))
print("O seu IMC é de: {:.1f}".format(imc))
if imc < 18.5:
    print(f"{nome}, você está ABAIXO do peso normal")
elif 18.5 <= imc < 25:
    print(f"Parabéns {nome}! Você está na faixa de PESO NORMAL")
elif 25 <= imc < 30:
    print(f"Atenção {nome}, você está com EXCESSO de peso.")
elif 30 <= imc < 40:
    print(f"Tenha cuidado {nome}, você está com OBESIDADE!")
elif imc >= 40:
    print(f"Bye, bye {nome}. OBESIDADE MÓRBIDA.")

print("Sua ingestão diária de água deve ser de: {:.1f} ml".format(agua_dia))