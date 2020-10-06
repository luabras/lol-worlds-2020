print("~~BEM VINDO AO LOL WORDS, INVOCADOR~~")

while True:
    escolha1 = input("""\n MENU INICIAL 
____________________________
Escolha sua opção
1 - Desejo ver a tabela de jogos - Fase de Grupos 
2 - Desejo ver a tabela de jogos - Fase Eliminatória 
3 - Mostrar Estatísticas dos Times 
4 - Mostrar Estatísticas dos Campeões
5 - Meus Palpites
►  """)

    if escolha1 == '1':
        while True:
            escolha1 = input("""~ Tabela de Jogos - Fase de Grupos ~
Escolha sua opção:
1 - Sábado  - 3 de outubro 
2 - Domindo - 4 de outubro 
3 - Segunda - 5 de outubro
4 - Terça   - 6 de outubro
5 - Quinta  - 8 de outubro
6 - Sexta   - 9 de outubro
7 - Sábado  - 10 de outubro
0 - Voltar para o menu anterior
►  """)
            if escolha1 == '1':
                print(""""~ Jogos do dia 03 - Sábado ~
                    5h - FlyQuest x Top Esports
                    6h - Unicorns of Love x DragonX
                    7h - Rogue x PSG Talon
                    8h - DAMWON Gaming x JD Gaming
                    9h - Gen.G x LGD Gaming
                    10h - TSM x Fnatic \n""")
                back = input("Digite enter para voltar pro menu anterior")


            elif escolha1 == '2':
                print("""~ Jogos do dia 04 - Domingo ~
                    5h - Machi Esports x Team Liquid
                    6h - G2 x Suning
                    7h - Rogue x DAMWON Gaming
                    8h - PSG Talon x JD Gaming
                    9h - Gen.G x TSM
                    10h - LGD Gaming x Fnatic \n""")
                back = input("Digite enter para voltar pro menu anterior")


            elif escolha1 == '3':
                print("""~ Jogos do dia 05 - Segunda ~
                    5h - Machi Esports x G2
                    6h - Team Liquid x Suning
                    7h - DAMWON Gaming x PSG Talon
                    8h - JD Gaming x Rogue
                    9h - FlyQuest x Unicorns of Love
                    10h - Top Esports x DragonX \n""")
                back = input("Digite enter para voltar pro menu anterior")


            elif escolha1 == '4':
                print("""~ Jogos do dia 06 - Terça ~
                    5h - G2 x Team Liquid
                    6h - Suning x Machi Esports
                    7h - DragonX x FlyQuest
                    8h - Top Esports x Unicorns of Love
                    9h - Fnatic x Gen.G
                    10h - TSM x LGD Gaming \n""")
                back = input("Digite enter para voltar pro menu anterior")

            elif escolha1 == '5':
                print("""~ Jogos do dia 08 - Quinta ~
                    5h - Team Liquid x G2
                    6h - Machi Esports x Suning
                    7h - G2 x Machi Esports
                    8h - Suning x Team Liquid
                    9h - Team Liquid x Machi Esports
                    10h - Suning x G2 \n""")
                back = input("Digite enter para voltar pro menu anterior")

            elif escolha1 == '6':
                print("""~ Jogos do dia 09 - Sexta ~
                    5h - PSG Talon x DAMWON Gaming
                    6h - Rogue x JD Gaming
                    7h - DAMWON Gaming x Rogue
                    8h - JD Gaming x PSG Talon
                    9h - PSG Talon x Rogue
                    10h - JD Gaming x DAMWON Gaming \n""")
                back = input("Digite enter para voltar pro menu anterior")

            elif escolha1 == '7':
                print("""~ Jogos do dia 10 - Sábado ~
                    5h - Fnatic x TSM
                    6h - LGD Gaming x Gen.G
                    7h - TSM x Gen.G
                    8h - Fnatic x LGD Gaming
                    9h - LGD Gaming x TSM
                    10h - Gen.G x Fnatic \n""")
                back = input("Digite enter para voltar pro menu anterior")

            elif escolha1 == '0':
                break

    if escolha1 == '2':
        while True:
            escolha1 = input("""~ Tabela de Jogos - Fase Eliminatória ~
Escolha sua opção:
1 - Quinta  - 15 de outubro 
2 - Sexta   - 16 de outubro 
3 - Sábado  - 17 de outubro
4 - Domingo - 18 de outubro
0 - Voltar para o menu anterior
►  """)
            if escolha1 == '1':
                seed1 = input ("Insira o vencedor do seed 1: ")
                seed2 = input("Insira o vencedor do seed 2: ")
                print ("7h - Quartas de Final 1 - {} x {}".format(seed1, seed2))
                back = input("Digite enter para voltar pro menu anterior")

            if escolha1 == '2':
                seed3 = input ("Insira o vencedor do seed 3: ")
                seed4 = input ("Insira o vencedor do seed 4: ")
                print ("7h - Quartas de Final 2 - {} x {}" .format(seed3, seed4))
                back = input("Digite enter para voltar pro menu anterior")

            if escolha1 == '3':
                seed5 = input ("Insira o vencedor do seed 5: ")
                seed6 = input ("Insira o vencedor do seed 6: ")
                print ("7h - Quartas de Final 3 - {} x {}" .format(seed5, seed6))
                back = input("Digite enter para voltar pro menu anterior")

            if escolha1 == '4':
                seed7 = input ("Insira o vencedor do seed 7: ")
                seed8 = input ("Insira o vencedor do seed 8: ")
                print ("7h - Quartas de Final 4 - {} x {}" .format(seed7, seed8))
                back = input("Digite enter para voltar pro menu anterior")






