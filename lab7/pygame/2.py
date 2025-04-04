import pygame
pygame.init()
screen = pygame.display.set_mode((1163, 535))

isDone = True
index = 0
sounds = [
    r"C:\Users\user\Desktop\python\lab7\pygame\Miyagi - Captain.mp3",
    r"C:\Users\user\Desktop\python\lab7\pygame\MiyaGi   Эндшпиль - Fire Man.mp3",
    r"C:\Users\user\Desktop\python\lab7\pygame\Виктор Цой - Группа крови.mp3",
]

color = (255, 255, 255)

isPaused = False
isPlayed = True
while isDone:
    screen.fill(color)
    pygame.display.update()
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            isDone = False

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            if index == len(sounds) - 1:
                index = 0
            else:
                index += 1
            isPaused = False
            isPlayed = True

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            if index == 0:
                index = len(sounds) - 1
            else:
                index -= 1
            isPaused = False
            isPlayed = True

        if event.type == pygame.KEYDOWN and isPlayed:
            if isPaused:
                pygame.mixer.music.unpause()
                isPaused = not isPaused
            else:
                pygame.mixer.music.load(sounds[index])
                pygame.mixer.music.play(2)
            isPlayed = not isPlayed

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not isPlayed:
            pygame.mixer.music.pause()
            isPlayed = not isPlayed
            isPaused = not isPaused

    pygame.display.flip()

# import pygame
# pygame.init()
# screen = pygame.display.set_mode((995, 535))

# isDone = True
# index = 0
# sounds = [
#     r"C:\Users\user\Desktop\python\lab7\pygame\Miyagi - Captain.mp3",
#     r"C:\Users\user\Desktop\python\lab7\pygame\MiyaGi   Эндшпиль - Fire Man.mp3",
#     r"C:\Users\user\Desktop\python\lab7\pygame\Виктор Цой - Группа крови.mp3",
# ]

# images = [
#     r"C:\Users\user\Desktop\python\lab7\pygame\Captain.png",
#     r"C:\Users\user\Desktop\python\lab7\pygame\fireMan.png",
#     r"C:\Users\user\Desktop\python\lab7\pygame\Группа Крови.png",
# ]

# color = (255, 255, 255)

# isPaused = False
# isPlayed = True

# def load_and_play_music(index):
#     pygame.mixer.music.load(sounds[index])
#     pygame.mixer.music.play(2)
#     image = pygame.image.load(images[index])
#     screen.blit(image, (0, 0))
#     pygame.display.update()

# load_and_play_music(index)

# while isDone:
#     for event in pygame.event.get():

#         if event.type == pygame.QUIT:
#             isDone = False

#         elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
#             if index == len(sounds) - 1:
#                 index = 0
#             else:
#                 index += 1
#             isPaused = False
#             isPlayed = True
#             load_and_play_music(index)

#         elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
#             if index == 0:
#                 index = len(sounds) - 1
#             else:
#                 index -= 1
#             isPaused = False
#             isPlayed = True
#             load_and_play_music(index)

#         if event.type == pygame.KEYDOWN and isPlayed:
#             if isPaused:
#                 pygame.mixer.music.unpause()
#                 isPaused = not isPaused
#             else:
#                 load_and_play_music(index)
#             isPlayed = not isPlayed

#         elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not isPlayed:
#             pygame.mixer.music.pause()
#             isPlayed = not isPlayed
#             isPaused = not isPaused

#     pygame.display.flip()

# pygame.quit()
