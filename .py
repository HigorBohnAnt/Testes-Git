import random
import time

def print_slow(text):
    """Imprime o texto lentamente para criar suspense."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()


print ("teste git alteracao sla sem ideia para colocar aqui")

def jogo_adivinhacao():
    print_slow("\nBem-vindo ao jogo de Adivinhação Mágica!")
    print_slow("Eu sou um mago computadorizado e escolhi um número entre 1 e 20.")
    print_slow("Será que você consegue adivinhar? Vamos descobrir!\n")

    numero_secreto = random.randint(1, 20)
    tentativas = 0

    while True:
        try:
            palpite = int(input("Digite seu palpite (entre 1 e 20): "))

            if palpite < 1 or palpite > 20:
                print_slow("Ei, está trapaceando? Escolha um número entre 1 e 20!")
                continue

            tentativas += 1

            if palpite < numero_secreto:
                print_slow("Hmm... muito baixo! Tente novamente.")
            elif palpite > numero_secreto:
                print_slow("Uau, muito alto! Tente de novo.")
            else:
                print_slow(f"\nIncrível! Você acertou o número secreto ({numero_secreto}) em {tentativas} tentativas!")

                if tentativas <= 3:
                    print_slow("Você é praticamente um mago das adivinhações!")
                elif tentativas <= 6:
                    print_slow("Nada mal, suas habilidades são impressionantes!")
                else:
                    print_slow("Finalmente! Eu estava começando a cochilar... mas bom trabalho!")
                break
        except ValueError:
            print_slow("Isso não é um número válido! Tente novamente com um número de 1 a 20.")

if __name__ == "__main__":
    jogar = "s"
    while jogar.lower() == "s":
        jogo_adivinhacao()
        jogar = input("\nQuer jogar novamente? (s/n): ")

    print_slow("\nObrigado por jogar! Até a próxima aventura mágica!\n")
