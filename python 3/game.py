

# import pygame
# import sys
# import random
# import pyttsx3
# import threading

# # Инициализация
# pygame.init()
# pygame.mixer.init()

# width, height = 600, 600
# screen = pygame.display.set_mode((width, height))
# pygame.display.set_caption("Guess the Color")

# # Цвета (только английские названия)
# COLORS = {
#     "RED": (255, 0, 0),
#     "GREEN": (0, 255, 0),
#     "BLUE": (0, 0, 255),
#     "YELLOW": (255, 255, 0),
#     "CYAN": (0, 255, 255),
#     "MAGENTA": (255, 0, 255),
#     "WHITE": (255, 255, 255),
#     "BLACK": (0, 0, 0),
#     "TEAL": (0, 128, 128),
#     "PURPLE": (128, 0, 128),
#     "AQUE": (0, 255, 255),
#     "BROWN": (128, 128, 128),
#     "JOK": (128, 0, 0),
#     "OOBA": (51, 51, 153)
# }

# # Озвучка в потоке
# def speak_color(color_name):
#     threading.Thread(target=_speak, args=(color_name,), daemon=True).start()

# def _speak(color_name):
#     engine = pyttsx3.init()
#     engine.setProperty('rate', 140)
#     engine.say(color_name)
#     engine.runAndWait()

# # Выбор случайного начального цвета
# color_keys = list(COLORS.keys())
# current_color = random.choice(color_keys)
# speak_color(current_color)

# # Главный цикл
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()

#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_r:
#                 current_color = "RED"
#             elif event.key == pygame.K_g:
#                 current_color = "GREEN"
#             elif event.key == pygame.K_b:
#                 current_color = "BLUE"
#             elif event.key == pygame.K_y:
#                 current_color = "YELLOW"
#             elif event.key == pygame.K_c:
#                 current_color = "CYAN"
#             elif event.key == pygame.K_m:
#                 current_color = "MAGENTA"
#             elif event.key == pygame.K_w:
#                 current_color = "WHITE"
#             elif event.key == pygame.K_k:
#                 current_color = "BLACK"
#             elif event.key == pygame.K_z:
#                 current_color = "TEAL"
#             elif event.key == pygame.K_p:
#                 current_color = "PURPLE"
#             elif event.key == pygame.K_a:
#                 current_color = "AQUE"
#             elif event.key == pygame.K_e:
#                 current_color = "BROWN"
#             elif event.key == pygame.K_u:
#                 current_color = "JOK"
#             elif event.key == pygame.K_i:
#                 current_color = "OOBA"

#             speak_color(current_color)

#     # Заливка экрана цветом
#     screen.fill(COLORS[current_color])
#     pygame.display.flip()