from time import sleep
from random import randint 

menu_jokempo2 = """
| Suas opções de jogada são: |
|                            |
| [0] Pedra 🗿               | 
| [1] Papel 📃               |
| [2] Tesoura ✂️              |
| [3] lagarto 🦎             |jokj
| [4] spok 🖖                |
"""

menu_inicial_jokempo = """
| Suas opções de jogada são: |
|                            |
| [0] Pedra 🗿               | 
| [1] Papel 📃               |
| [2] Tesoura ✂️             |
"""

#JOKEMPO PADRÃO
def jokempo_portugues():

    itens = ('Pedra','Papel','Tesora')
    computador = randint(0, 2)

    while True: 

        print("Bem-vindo ao queridissímo JOKENPÔ ")
        print(menu_inicial_jokempo)
        jogador = int(input(" Qual é a sua jogada ? "))

        print("")
        print("JO")
        sleep(1)
        print("KEN")
        sleep(1)
        print("PÔ")
        print("")
        print('-='*15)

        print(f'jogador jogou: {itens[jogador]}')
        print(f'computador jogou: {itens[computador]}')
        print('-='*15)

        if computador == jogador:
            print("Empate!")
            
        if computador == 0:
            if jogador == 1:
                print('Boa, você ganhou!')

            elif jogador == 2:
                print('Droga, você perdeu!')
    
        if computador == 1:
            if jogador == 0:
                print('Droga, você perdeu!')

            elif jogador == 2:
                print('Boa, você ganhou!')
        
        if computador == 2:
            if jogador == 0:
                print('Boa, você ganhou!')

            elif jogador == 1:
                print('Droga, você perdeu!')

        print("")
        jogar = input("quer continuar jogando?")
        if jogar == ("sim"):
            continue

        else:
            print("")
            print("Finalizando o jogo")
            break
        
#JOKEMPO 2
def jokempo_2():

    itens = ('Pedra','Papel','Tesora','lagarto','spok')
    computador = randint(0, 4)

    while True: 

        print("Bem-vindo ao queridissímo JOKENPÔ ")
        print(menu_jokempo2)
        jogador = int(input(" Qual é a sua jogada ? "))

        print("")
        print("JO")
        sleep(1)
        print("KEN")
        sleep(1)
        print("PÔ")
        print("")
        print('-='*15)

        print(f'jogador jogou: {itens[jogador]}')
        print(f'computador jogou: {itens[computador]}')
        print('-='*15)

        if computador == jogador:
            print("Empate!")
            
        if computador == 0:
            if jogador == 1:
                print('Boa, você ganhou!')

            elif jogador == 2:
                print('Droga, você perdeu!')

            elif jogador == 3:
                print('Boa, você ganhou!')

            elif jogador == 4:
                print('Droga, você perdeu!')        
    
        if computador == 1:
            if jogador == 0:
                print('Droga, você perdeu!')

            elif jogador == 2:
                print('Boa, você ganhou!')

            elif jogador == 3:
                print('Droga, você perdeu!')

            elif jogador == 4:
                print('Boa, você ganhou!')
        
        if computador == 2:
            if jogador == 0:
                print('Boa, você ganhou!')

            elif jogador == 1:
                print('Droga, você perdeu!')

            elif jogador == 3:
                print('Droga, você perdeu!')

            elif jogador == 4:
                print('Boa, você ganhou!')

        if computador == 3:
            if jogador == 0:
                print('Boa, você ganhou!')

            elif jogador == 1:
                print('Droga, você perdeu!')

            elif jogador == 2:
                print('Boa, você ganhou!')

            elif jogador == 4:
                print('Droga, você perdeu!')

        if computador == 4:
            if jogador == 0:
                print('Droga, você perdeu!')

            elif jogador == 1:
                print('Boa, você ganhou!')

            elif jogador == 2:
                print('Droga, você perdeu!')

            elif jogador == 3:
                print('Boa, você ganhou!')

        print("")
        jogar = input("quer continuar jogando?")
        if jogar == ("sim"):
            continue

        else:
            print("")
            print("Finalizando o jogo")
            return 

#JOKEMPO JAPONÊS     
def jokempo_japones():
    itens = ('石 (Ishi)', '紙 (Kami)', 'はさみ (Hasami)')
    computador = randint(0, 2)

    while True:
        print("じゃんけんポーへようこそ！")
        print("")
        print('''選択肢：
[0] 石 (Ishi) 
[1] 紙 (Kami) 
[2] はさみ (Hasami) ''')

        jogador = int(input("あなたの選択は？"))

        print("")
        print("JAN")
        sleep(1)
        print("KEN")
        sleep(1)
        print("PON")
        sleep(2)
        print("")
        print('-=' * 15)

        print(f'コンピューターの選択: {itens[computador]}')
        print(f'あなたの選択: {itens[jogador]}')
        print('-=' * 15)

        if computador == jogador:
            print('あいこでした！')

        if computador == 0:
            if jogador == 1:
                print('おめでとうございます！あなたの勝ちです！')

            elif jogador == 2:
                print('残念！あなたの負けです！')

        elif computador == 1:
            if jogador == 0:
                print('残念！あなたの負けです！')

            elif jogador == 2:
                print('おめでとうございます！あなたの勝ちです！')

        elif computador == 2:
            if jogador == 0:
                print('おめでとうございます！あなたの勝ちです！')

            elif jogador == 1:
                print('残念！あなたの負けです！')

        print("")
        jogar = input("ゲームを続けますか？")
        if jogar == ("hai"):
            continue
        else:
            print("")
            print("ゲームを終了します")
            break


#INICIANDO O JOGO
print("Bem vindo o que gostaria de jogar?")
jogo = input('Jokempo ou Jokempo 2 ?')
if jogo == ("jokempo"):
    print("JOKENPÔ!")
    print("")
    idioma = input("""Qual o idioma que você deseja jogar?
    Português ou Japones""")
    sleep(1)
    if idioma == "portugues":
        jokempo_portugues()

    elif idioma == "japones":
        jokempo_japones() 
    else:
        print("Escolha um dos dois idioma, burrão!")

elif jogo == ("jokempo 2"):
    print("JOKENPÔ 2!")
    print("")
    sleep(1)
    jokempo_2()        