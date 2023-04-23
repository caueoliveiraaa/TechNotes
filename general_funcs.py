import sys
from termcolor import colored
import pyautogui as p
import pyperclip


def display_error(error=''):
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = exc_tb.tb_frame.f_code.co_filename
    error_msg = f"\nError: {error}" 
    error_msg += f"\nError Type: {exc_type}" 
    error_msg += f"\nError Description: {exc_obj}" 
    error_msg += f"\nError File: {fname}"
    error_msg += f"\nError Line: {exc_tb.tb_lineno}" 
    print(colored(error_msg, 'red'))
    return error_msg


def locate_image(file_path, secs, ima_name, exc=True, gray=False, move_mouse=False, area=(0, 0, 1920, 1080), send_keys='', press_enter=False, conf=0.9, clicks=0, up=0, down=0, left=0, right=0):
    loop_counter = 0
    while loop_counter < secs:
        image = p.locateCenterOnScreen(image=file_path, confidence=conf, grayscale=gray, region=area)

        if image:
            print(f'\nfound {ima_name}') if loop_counter != 0 else print(f'found {ima_name}') 
            x_pos, y_pos = image

            x_pos += right
            x_pos -= left
            y_pos += down
            y_pos -= up

            if clicks == 0:
                if move_mouse is True:
                    p.moveTo(x_pos, y_pos)

                if send_keys:
                    pyperclip.copy(send_keys)
                    p.hotkey('ctrl', 'v')
                    p.sleep(0.2)

                if press_enter is True:
                    p.press('enter')

                return x_pos, y_pos

            elif clicks == 1:
                p.click(x_pos, y_pos)
                p.sleep(0.1)

                if send_keys:
                    pyperclip.copy(send_keys)
                    p.hotkey('ctrl', 'v')
                    p.sleep(0.2)

                if press_enter is True:
                    p.press('enter')

                return x_pos, y_pos

            elif clicks == 2:
                p.doubleClick(x_pos, y_pos)
                p.sleep(0.1)

                if send_keys:
                    pyperclip.copy(send_keys)
                    p.hotkey('ctrl', 'v')
                    p.sleep(0.2)

                if press_enter:
                    p.press('enter')

                return x_pos, y_pos

            elif clicks >= 3:
                for c in range(clicks):
                    p.click(x_pos, y_pos)
                    p.sleep(0.1)
                    print(f'clicked {c+1}')

                return x_pos, y_pos

        p.sleep(1)
        loop_counter += 1
        print(f'searching for {ima_name} - {loop_counter}', end='\r')

    if (loop_counter >= secs) and (exc is True):
        raise ValueError(f'image {ima_name} not found')
    