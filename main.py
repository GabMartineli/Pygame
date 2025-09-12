import pygame


print('Iniciando janela')
pygame.init()
screen = pygame.display.set_mode(size = (700, 520))


print('Iniciando laço')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Fechando janela')
            pygame.quit() # fechar janela
            quit() # fechar jogo
            