import pygame, random
from pygame.locals import *

def main():

    def pos_grid(): #Gera uma posição no grid 20x20
        x = 0
        y = 0
        
        while x <= 160 and y <= 40 or x <= 100 and y >= 560: #Evita que a maçã apareça sobre os textos da esquerda
            x = random.randint(0, 780) 
            y = random.randint(0, 580)
        
        return (x // 20 * 20, y // 20 * 20)

    def collision(c1, c2): #Testa colisões
        return (c1[0] == c2[0] and c1[1] == c2[1])

    pygame.init()

    tela = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Jogo da Cobra')
    fps = pygame.time.Clock()

    #Cores
    branco = (255, 255, 255)
    preto = (0, 0, 0)
    vermelho = (250, 0, 0)

    #Texto
    fonte = pygame.font.SysFont(pygame.font.get_default_font(), 45)
    fonte_2 = pygame.font.SysFont(pygame.font.get_default_font(), 30) #Autoria
    texto_derrota = fonte.render('GAME OVER', 1, vermelho)
    texto_pause = fonte.render('PAUSE', 1, branco)
    texto_autor = fonte_2.render('@fpeduu', 1, branco) #Autoria
    texto_tutorial = fonte_2.render('SETAS = MOVIMENTO', 1, branco)
    texto_tutorial2 = fonte_2.render('SPACE = PAUSE', 1, branco)
    inicio = True
    pts = 0

    #Player
    player = pygame.Surface((20, 20))
    player.fill(branco)
    player_pos = [[400, 400], [400, 420], [400, 440]]
    dir = 'stopped' #Direção do player
    last_dir = 'none'
    pressed = False
    vivo = True

    #Comida da cobra
    apple = pygame.Surface((20, 20))
    apple.fill(vermelho)
    apple_pos = pos_grid()
    
    #Áudio
    #plun = pygame.mixer.Sound('audio/plun.ogg')
    #morte = pygame.mixer.Sound('audio/rewind.ogg')
    #count_som = 1

    while True:
        for event in pygame.event.get(): #Testa os eventos
            if event.type == QUIT:
                pygame.quit()
            
            if event.type == KEYDOWN:
                if vivo == True:
                    if event.key == K_UP: #Direção da cobra
                        if dir == 'down' or last_dir == 'down' or dir == 'up': #Impede que a cobra se atravesse
                            pass
                        elif pressed == True: #Resolve o BUG (Olhar última linha)
                            pass
                        else:
                            dir = 'up'
                            last_dir = 'stopped'
                            pressed = True
                    if event.key == K_DOWN:
                        if dir == 'up' or last_dir == 'up' or dir == 'down':
                            pass
                        elif pressed == True or inicio == True:
                            pass
                        else:
                            dir = 'down'
                            last_dir = 'stopped'
                            pressed = True
                    if event.key == K_LEFT:
                        if dir == 'right' or last_dir == 'right' or dir == 'left':
                            pass
                        elif pressed == True:
                            pass
                        else:
                            dir = 'left'   
                            last_dir = 'stopped'
                            pressed = True
                    if event.key == K_RIGHT:
                        if dir == 'left' or last_dir == 'left' or dir == 'right':
                            pass
                        elif pressed == True:
                            pass
                        else:
                            dir = 'right'
                            last_dir = 'stopped'
                            pressed = True
                    if event.key == K_SPACE: #Pausa e despausa
                        if not dir == 'stopped':
                            last_dir = dir
                            dir = 'stopped'
                        elif dir == 'stopped' and last_dir == 'none':
                            pass
                        else:
                            dir = last_dir
                            last_dir = 'stopped'
                    if pressed == True and inicio == True:
                        inicio = False
                else:
                    pass

        #Limpando a tela (IMPORTANTE)
        tela.fill(preto)

        #Colisão Player-Maçã
        if collision(player_pos[0], apple_pos): 
        #    plun.play()
            apple_pos = pos_grid()
            player_pos.append([0, 0]) 
            pts += 1

        #Colisão Player-Player
        for c in range(len(player_pos) - 2, 0 , -1):
            if collision(player_pos[0], player_pos[c]):
                vivo = False
        
        #Verifica se o player está saindo da tela
        if player_pos[0][0] == 0 and dir == 'left': #Dividi em várias linhas para não ficar feio
            vivo = False
        if player_pos[0][0] == 780 and dir == 'right':
            vivo = False
        if player_pos[0][1] == 0 and dir == 'up':
            vivo = False
        if player_pos[0][1] == 580 and dir == 'down':
            vivo = False

        #Verifica se o player está vivo
        if vivo == False:
            dir = 'stopped'
            tela.blit(texto_derrota, [300, 0])
        #    if count_som > 0:
        #        morte.play()
        #        count_som -= 1

        #Atualizando as posições do corpo da cobra
        for c in range(len(player_pos) - 1, 0, -1): 
            if dir == 'stopped':
                pass
            else:
                (player_pos[c][0], player_pos[c][1]) = (player_pos[c-1][0], player_pos[c-1][1])
        
        #Atualiza a posição da cabeça da cobra com base na direção
        if dir == 'up':
            player_pos[0][1] -= 20
        if dir == 'down':
            player_pos[0][1] += 20
        if dir == 'left':
            player_pos[0][0] -= 20
        if dir == 'right':
            player_pos[0][0] += 20
        if dir == 'stopped':
            player_pos = player_pos
            if inicio == False and vivo == True:
                tela.blit(texto_pause, [335, 280])
            if vivo == True:
                tela.blit(texto_tutorial, [560, 10])
                tela.blit(texto_tutorial2, [560, 35])  
        
        #Gerando os elementos da tela
        tela.blit(apple, apple_pos) #Gera a maçã
        for pos in player_pos: #Gerar a cobra
            tela.blit(player, pos)
         
        tela.blit(texto_autor, [5, 570])
        texto = fonte.render(f'POINTS: {pts}', 1, branco)
        tela.blit(texto, [0, 0])
        
        pressed = False

        #Quantidade de vezes que a tela é atualizada em um segundo
        fps.tick(11)
        pygame.display.update()

main()

#BUG = A cobra pode se atravessar (e morrer) se a direção for mudada rapidamente (Resolvido)