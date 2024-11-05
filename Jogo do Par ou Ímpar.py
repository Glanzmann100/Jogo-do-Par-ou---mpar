import random

#Solicita a escolha do jogador
Jogador_Escolha = input("Par ou Impar? ")
Jogador_Numero = int(input("Escolha um número entre 0 a 10: "))
Adversário = random.randint(0,10)

#Estabelece a soma e o resultado
Soma = Jogador_Numero + Adversário
Resultado = "Par" if Soma % 2 == 0 else "Impar"

print(f"Número do Adversário: {Adversário}") 
print(f"Soma: {Soma}")
print(f"Resultado: {Resultado}")

#Verifica quem ganhou
if Jogador_Escolha == Resultado: 
    print("Você venceu!") 
else: 
    print("Você perdeu!")