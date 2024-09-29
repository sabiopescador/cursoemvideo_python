
import pyfiglet
from colorama import Fore, Style, init
import random

# Inicialize o Colorama
init(autoreset=True)

# Defina as cores disponíveis
colors = {
    'red': Fore.RED,
    'green': Fore.GREEN,
    'yellow': Fore.YELLOW,
    'blue': Fore.BLUE,
    'magenta': Fore.MAGENTA,
    'cyan': Fore.CYAN,
    'white': Fore.WHITE,
    'orange': '\033[38;5;214m'  # ANSI escape code para um tom laranja
}

# Lista de fontes disponíveis
FONTS = [
    'slant', 'block', '4max', 'digital', 'isometric1',
    '1row', 'isometric3', 'isometric4', 'rectangles',
    '3d-ascii', 'amc_3_line', 'banner', 'amc_slider', 'amc_thin',
    '5lineoblique', 'big', 'small', 'standard', 'thinkertoy', 
    'twisted'
]

def colorful_text(text, font='slant', color='white', width=80):
    if font not in FONTS:
        print(f"Fonte '{font}' não está disponível. Usando 'slant' como padrão.")
        font = 'slant'

    # Verifique se a cor está no dicionário de cores
    color_code = colors.get(color, Fore.WHITE)  # Usar branco como padrão

    # Gerar o texto com Pyfiglet com largura máxima definida
    figlet = pyfiglet.Figlet(font=font, width=width)
    ascii_art = figlet.renderText(text)

    colored_text = ''
    for char in ascii_art:
        if char.strip():  # Apenas colorir caracteres que não são espaços em branco
            colored_text += color_code + char
        else:
            colored_text += char  # Manter os espaços em branco sem cor

    return colored_text

