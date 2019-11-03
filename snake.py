import pygame

pygame.init()

white = (255,255,255) #branco rgb
black = (0,0,0) #preto rgb
red = (255,0,0) #vermelho rgb

display_width = 800
display_height = 600

fps = 60

clock = pygame.time.Clock()

#tamanhoecra
gameDisplay = pygame.display.set_mode((display_width,display_height))

#titulo
pygame.display.set_caption("Slither")

pygame.display.update()

gameExit = False

lead_x = display_width/2 #numberofblocksqvaiestar

lead_y = display_height/2 #numberofblocksqvaiestar

lead_x_change = 0 #pixeisqandahorizontal

lead_y_change = 0 #pixeisqandavertical

block_size = 5 #aquioqanda

#enquanto o gameexit ñ é true

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change = -block_size #pixeisqanda
                lead_y_change = 0
            elif event.key == pygame.K_RIGHT:
                lead_x_change = block_size
                lead_y_change = 0
            elif event.key == pygame.K_UP:
                lead_y_change = -block_size
                lead_x_change = 0
            elif event.key == pygame.K_DOWN:
                lead_y_change = block_size
                lead_x_change = 0

    if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
        gameExit = True


    lead_x += lead_x_change
    lead_y += lead_y_change

    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay ,black, [lead_x,lead_y,10,10])  #primeirosdoisposiçoes, segundodoistamanho
    pygame.display.update()
    clock.tick(fps)#metesaquiosfps #maisfpsgastamaisprocessador,emcasodedesgastemetomaispixeisdecadavez

    # gameDisplay.fill (red , rect= [200,200,50,50] ) #desenhar coisas no ecra

pygame.quit()

quit()

#TUTORIAL14