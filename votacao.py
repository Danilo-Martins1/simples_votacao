from rich import print
import os

# Constantes
# Apresentar Os Candidatos
VOTOS_DANILO = 0
VOTOS_GUSTAVO = 0
VOTOS_LARISSA = 0
# Rodar Infinitamente
while True:
    print('='*25)
    print(f'[on #d78700]VOTOS DANILO =[/] {VOTOS_DANILO}{os.linesep}[on red]VOTOS GUSTAVO =[/] {VOTOS_GUSTAVO}{os.linesep}[on #5f00af]VOTOS LARISSA =[/] {VOTOS_LARISSA}')
    print('='*25)
    # Permitir Votar
    try:
        votos = int(input(f'QUEM DEVE SER O CAPITÃO DO TIME ?{os.linesep}1 - DANILO{os.linesep}2 - GUSTAVO{os.linesep}3 - LARISSA{os.linesep}Seu Voto: '))
        # #Loop
        if votos == 1:
            VOTOS_DANILO += 1
        elif votos == 2:
            VOTOS_GUSTAVO += 1
        elif votos == 3:
            VOTOS_LARISSA += 1
        else:
            print('Acabou A Votação')
    except:
        print('Digite Apenas Numeros')
    os.system('cls')
