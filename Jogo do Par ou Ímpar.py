import random

#Solicita a escolha do jogador
Jogadas = 0
Jogador = 0
Adversário = 0 
Rodadas = 3

while True:
    Jogador_Escolha = input("Par ou Impar? ")
    Jogador_Numero = int(input("Escolha um número entre 0 a 10: "))
    Adversário = random.randint(0,10)
    Soma = Jogador_Numero + Adversário
    Resultado = "Par" if Soma % 2 == 0 else "Impar"

    print(f"Número do Adversário: {Adversário}") 
    print(f"Soma: {Soma} Resultado: {Resultado}")

    if Jogador_Escolha == Resultado:
        Jogador += 1
        print("Você venceu")
    else:
        Adversário += 1
        print("Você perdeu!")
    
    print(f"Placar: Jogador {Jogador} x {Adversário} Computador")

    if Jogador == Rodadas:
        print("Parabéns você venceu o jogo")
        break
    elif Adversário == Rodadas:
        print("O Adversário venceu o jogo")
        break
