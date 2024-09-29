import pyfiglet
from colorama import Fore, Style, init

# Inicialize o Colorama
init(autoreset=True)

# Defina uma cor específica para todo o texto
chosen_color = Fore.BLUE  # Escolha a cor que você quiser, ex: Fore.RED, Fore.GREEN

# Gerar o texto com Pyfiglet
figlet = pyfiglet.Figlet(font='slant')  # Escolha a fonte que preferir
text = figlet.renderText('CONDICOES ANINHADAS')

# Colorir o texto todo com a cor escolhida
colored_text = ''

for char in text:
    if char.strip():  # Apenas colorir os caracteres que não são espaços em branco
        colored_text += chosen_color + char
    else:
        colored_text += char  # Manter os espaços em branco sem cor

print(colored_text)
