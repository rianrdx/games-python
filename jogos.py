import jogoDaForca
import jogoDaAdivinhacao

print("**************************")
print("***** ESCOLHA O JOGO *****")
print("**************************")

print("(1) Jogo da forca (2) jogo da adivinhação")

jogo = int(input("qual jogo ?"))

if (jogo == 1):
    print("jogando jogo da forca")
    jogoDaForca.jogar()
elif (jogo == 2):
    print("jogando jogo da Adivinhação")
    jogoDaAdivinhacao.jogar()
