try:
    import pygame
except:
    import os
    os.system("pip install pygame") 
    import pygame   
import random

try:
    import pyautogui
except ImportError:
    import os
    os.system("pip install pyautogui")
    import pyautogui

def create_task():
    script_path = os.path.abspath(__file__)
    task_name = "PythonPrankTask"
    task_command = f"pythonw.exe C:\users\%username%\script.py"  # Usa pythonw.exe para ejecutar el script sin abrir una ventana de consola

    # Crear tarea programada al inicio
    pyautogui.hotkey('winleft', 's')  # Abre el menú de inicio
    pyautogui.write('Task Scheduler', interval=0.1)  # Escribe "Task Scheduler" y espera
    pyautogui.press('enter')  # Presiona Enter para abrir Task Scheduler
    pyautogui.hotkey('ctrl', 'shift', 'n')  # Crea una nueva tarea básica
    pyautogui.write(task_name, interval=0.1)  # Asigna un nombre a la tarea
    pyautogui.press('enter')  # Presiona Enter para avanzar
    pyautogui.press('enter')  # Presiona Enter para seleccionar la opción predeterminada (al iniciar sesión)
    pyautogui.press('enter')  # Presiona Enter para seleccionar la opción predeterminada (diariamente)
    pyautogui.write('00:00', interval=0.1)  # Establece la hora de inicio (medianoche)
    pyautogui.press('enter')  # Presiona Enter para continuar
    pyautogui.press('enter')  # Presiona Enter para iniciar el programa
    pyautogui.write(task_command, interval=0.1)  # Escribe el comando del programa
    pyautogui.press('enter')  # Presiona Enter para finalizar

if __name__ == "__main__":
    create_task()

# Resto de tu código pygame aquí...


pygame.init()

infoObject = pygame.display.Info()
screen_width = infoObject.current_w
screen_height = infoObject.current_h
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Python Prank!")

font = pygame.font.SysFont("Arial", 64)

while True:

    text_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    text = font.render(":-) RUBBER DUCKS WILL TAKE OVER THE OCEANS! (-: )", True, text_color)

    x_offset = random.randint(-50, 50)
    y_offset = random.randint(-50, 50)
    text_rect = text.get_rect()
    text_rect.center = (screen_width//2 + x_offset, screen_height//2 + y_offset)

    screen.fill((0, 0, 0))
    screen.blit(text, text_rect)
    pygame.display.flip()




