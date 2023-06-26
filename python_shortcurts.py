

# Printar cores:
def print_colors_py() -> None:
    """ Printar cores do python de forma numerica """

    colors = {
        'black': '\033[030m',
        'red': '\033[031m',
        'green': '\033[032m',
        'yellow': '\033[033m',
        'blue': '\033[034m',
        'magenta': '\033[035m',
        'cyan': '\033[036m',
        'white': '\033[037m'
    }

    for color_name, color_code in colors.items():
        print(f"{color_code}{color_name}\033[0m")




# Modificar print:
from datetime import datetime
import builtins
import sys


def set_output() -> None:
    """ Printar datetime atual e funcao onde esta o print """

    original_print = builtins.print
    def costumized_output(*args, **kwargs):
        current_time = datetime.now().strftime("%H:%M:%S")
        frame = sys._getframe()
        output_msg = f'\033[95m[{current_time}]:\033[0m \033[94m{frame.f_back.f_code.co_name}:\033[0m'
        original_print(output_msg, *args, **kwargs)
    builtins.print = costumized_output





# Printar erro:
import sys


def display_error() -> str:
    """ Mostrar mensagem de erro com detalhes """

    exctp, exc, exctb = sys.exc_info()
    message = f'\ntraceback:{exctb.tb_frame.f_code.co_name}:{exctb.tb_lineno}:{exctp}:'
    message_error += f'{exc}\n'

    print('\033[33m' + message + '\033[0m', end='')
    print('"\033[33m' + message_error + '\033[0m"')

    return f'traceback:{exctb.tb_frame.f_code.co_name}:{exctb.tb_lineno}:{exctp}:"{exc}"'





# Printar posicao do mouse:
import pyautogui as p
import os


def print_mouse_position(interval=1) -> None:
    os.system('cls')
    print(f'Screen size: {p.size()}')

    counter = 0
    while True:
        counter += 1

        if counter == 10:
            os.system('cls')
            counter = 0

        x, y = p.position()
        print(f'Mouse position: x={x}, y={y}')
        p.sleep(interval)



# Calcular tempo de execucao da tarefa com decorador:
import time

def measure_time(func):
    """ Operador para calcular quanto tempo uma funcao leva para iniciar e terminar """

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        total_time = end_time - start_time
        hours, rem = divmod(total_time, 3600)
        minutes, seconds = divmod(rem, 60)

        if hours > 0:
            print(f"Function '{func.__name__}' took {int(hours)} hours, {int(minutes)} minutes, e {seconds:.2f} seconds to execute.")
        elif minutes > 0:
            print(f"Function '{func.__name__}' took {int(minutes)} minutes, e {seconds:.2f} seconds to execute.")
        else:
            print(f"Function '{func.__name__}' took {total_time:.2f} seconds to execute.")
        return result
    return wrapper



# Esvaziar diretorio(s):
import os


def clear_dirs(path='', paths=[]) -> None:
    """ Esvaziar diretorios """

    if not paths:
        if os.listdir(path):
            for file in os.listdir(path):
                os.remove(path + file)
                print(f'Removed "{file}" from "{path}"')
    else:
        for path in paths:
            if os.listdir(path):
                for file in os.listdir(path):
                    os.remove(path + file)
                    print(f'Removed "{file}" from "{path}"')