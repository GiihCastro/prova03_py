numero_secreto = 7

tentativas_maximas = 3

tentativas = 0

while tentativas < tentativas_maximas:
    try:
        palpite = int(input("Adivinhe o número (entre 1 e 10), você possui 3 tentativas: "))
        tentativas += 1

        if palpite == numero_secreto:
            print("Parabéns! Você acertou o número!")
            break
        else:
            print("Errado! Tente novamente.")

    except ValueError:
        print("Por favor, insira um número válido.")

else:
    print(f"Que pena! Você esgotou suas tentativas. O número era {numero_secreto}.")