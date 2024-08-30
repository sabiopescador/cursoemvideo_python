# Instalação das bibliotecas
# pip install rich pyfiglet
# pip install termcolor
# pip install colorama

# Importando os módulos
import colorama
import pyfiglet
from termcolor import colored
from colorama import Fore, Back, Style

colorama.init(autoreset=True)  # Reseta a cor do texto toda vez que imprime uma letra

# Definindo as cores válidas
cores_validas = { # dicio
    'azul': 'blue',
    'azul-claro': 'light_blue',
    'azul-escuro': 'cyan',
    'vermelho': 'red',
    'vermelho-escuro': 'dark_red',
    'rosa': 'magenta',
    'rosa-choque': 'light_magenta',
    'verde': 'green',
    'verde-claro': 'light_green',
    'verde-escuro': 'dark_green',
    'amarelo': 'yellow',
    'amarelo-ouro': 'light_yellow',
    'preto': 'grey',
    'preto-fosco': 'light_grey',
    'branco': 'white',
    'branco-neve': 'light_white',
    'cinza': 'grey',
    'cinza-chumbo': 'dark_grey',
    'laranja': 'light_red',
    'laranja-queimado': 'dark_red',
    'roxo': 'magenta',
    'roxo-escuro': 'dark_magenta',
    'marrom': 'yellow',
    'marrom-café': 'light_yellow',
    'bege': 'light_yellow',
    'bege-claro': 'white',
    'bordô': 'light_red',
    'turquesa': 'cyan',
    'salmon': 'light_red',
    'violeta': 'magenta'
}

msg = str.upper(input('Qual nome você quer escolher? ')) #coletando inputs do usuário
cor = str.lower(input('Agora escolha uma cor: '))

while cor not in cores_validas: # verificando a cor válida
    cor = str.lower(input('\033[1;30;41mEscolha uma cor válida!\033[m'))

formated_ascii = pyfiglet.figlet_format(msg, font='slant') # inserindo formatação

colored_ascii = colored(formated_ascii, cores_validas[cor]) # colocando cor na formatação usando os valores contidos no dicionário
print(colored_ascii)

print('\033[1;30;41mLetra branca com fundo vermelho\033[m')  # cores ANSI
print('\033[1;31;43mLetra vermelha fundo amarelo, em negrito\033[m')
print('\033[4;30;45mLetra branca, fundo lilás, sublinhado\033[m')
print('\033[1;37mLetra branca, fundo preto\033[m')
print('\033[7;37mLetra branca, fundo preto invertida\033[m')
print('Muito prazer em te conhecer {}{}{}!!'.format('\033[7;34;40m',msg,'\033[m'))

# módulo do colocama! :D
print(f'{Fore.BLUE}ha{Fore.RED}HA{Fore.YELLOW}ha{Fore.LIGHTGREEN_EX}HA{Fore.MAGENTA}ha{Fore.CYAN}HA{Fore.WHITE}ha{Fore.LIGHTYELLOW_EX}HA{Fore.LIGHTRED_EX}ha{Fore.LIGHTBLUE_EX}HA!\033[m xD')  # colorama library
print('')
print('Ta bom, a parte da letra grande eu admito que roubei dos tutoriais ai, mas a ideia geral foi minha heim .-. \n\nMas esse projeto vai continuar! xD')