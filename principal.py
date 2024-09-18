import pygame
import os
pygame.font.init()
pygame.mixer.init()

LARGURA, ALTURA = 900, 500
JAN = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Miau Miwar!")

BRANCO = (255, 255, 255)

BORDA = pygame.Rect(LARGURA//2 - 5, 0, 10, ALTURA)
PRETO = (0,0,0)

FPS = 60
VEL = 5
FOGO_VEL = 7
GATO_ALTURA, GATO_LARGURA= 55,55

MAX_FOGO = 3

VERMELHO_ACERTADO = pygame.USEREVENT + 1
AZUL_ACERTADO = pygame.USEREVENT + 2

VIDA_FONTE = pygame.font.SysFont('comicsans', 40)
GANHADOR_FONTE = pygame.font.SysFont('comicsans', 40)

GATO_VERMELHO_IMAGEM = pygame.image.load(os.path.join('Recursos', 'cat2_base_red.png'))
GATO_VERMELHO = pygame.transform.scale(GATO_VERMELHO_IMAGEM, (GATO_ALTURA, GATO_LARGURA))

GATO_AZUL_IMAGEM = pygame.image.load(os.path.join('Recursos', 'cat2_base_blue.png'))
GATO_AZUL = pygame.transform.scale(GATO_AZUL_IMAGEM, (GATO_ALTURA, GATO_LARGURA))

FOGO_VERMELHO_IMAGEM = pygame.image.load(os.path.join('Recursos', 'energy_effect_base_red.png'))
FOGO_VERMELHO = pygame.transform.scale(FOGO_VERMELHO_IMAGEM, (GATO_ALTURA/3, GATO_LARGURA/3))

FOGO_AZUL_IMAGEM = pygame.image.load(os.path.join('Recursos', 'energy_effect_base_blue.png'))
FOGO_AZUL = pygame.transform.scale(FOGO_AZUL_IMAGEM, (GATO_ALTURA/3, GATO_LARGURA/3))


FUNDO = pygame.transform.scale(pygame.image.load(os.path.join('Recursos', 'fundo.png')), (LARGURA, ALTURA))


SOM_FOGO_BOOM = pygame.mixer.Sound(os.path.join('Recursos', 'som1.mp3'))
SOM_FOGO_TIRO = pygame.mixer.Sound(os.path.join('Recursos', 'som2.wav'))



def desenhar_janela(vermelho, azul, fogos_vermelho, fogos_azul, vida_vermelho, vida_azul ):
    JAN.blit(FUNDO, (0,0))
    pygame.draw.rect(JAN, PRETO, BORDA)


    JAN.blit(VIDA_FONTE.render("S2 " + str(vida_vermelho), 1, BRANCO), (13,13))

    JAN.blit(VIDA_FONTE.render("S2 " + str(vida_azul), 1, BRANCO), ((LARGURA - (13*6)), 13))


    JAN.blit(GATO_VERMELHO, (vermelho.x, vermelho.y))
    JAN.blit(GATO_AZUL, (azul.x, azul.y))
    
    

    for fogo in fogos_azul:
        JAN.blit(FOGO_AZUL, (fogo.x , fogo.y), )

    for fogo in fogos_vermelho:
        JAN.blit(FOGO_VERMELHO, (fogo.x , fogo.y), )



    pygame.display.update()

def movimentar_vermelho(tecla_pressionada, vermelho):
    if tecla_pressionada[pygame.K_a] and vermelho.x - VEL > 0 :
        vermelho.x -= VEL
    if tecla_pressionada[pygame.K_d] and (vermelho.x + VEL + vermelho.width ) < BORDA.x + 10 :
        vermelho.x += VEL
    if tecla_pressionada[pygame.K_w] and vermelho.y - VEL > 0:
        vermelho.y -= VEL
    if tecla_pressionada[pygame.K_s] and vermelho.y + VEL + vermelho.height < ALTURA :
        vermelho.y += VEL

def movimentar_azul(tecla_pressionada, azul):
    if tecla_pressionada[pygame.K_LEFT] and azul.x - VEL > BORDA.x + 10 :
        azul.x -= VEL
    if tecla_pressionada[pygame.K_RIGHT] and (azul.x + VEL + azul.width) < LARGURA   :
        azul.x += VEL
    if tecla_pressionada[pygame.K_UP] and azul.y - VEL > 0:
        azul.y -= VEL
    if tecla_pressionada[pygame.K_DOWN] and azul.y + VEL + azul.height < ALTURA :
        azul.y += VEL


def controlhe_fogo(fogos_vermelho, fogos_azul, vermelho, azul):
    for fogo in fogos_vermelho:
        fogo.x += FOGO_VEL
        if azul.colliderect(fogo):
            pygame.event.post(pygame.event.Event(AZUL_ACERTADO))
            fogos_vermelho.remove(fogo)
        elif fogo.x > LARGURA:
            fogos_vermelho.remove(fogo)

    for fogo in fogos_azul:
        fogo.x -= FOGO_VEL
        if vermelho.colliderect(fogo):
            pygame.event.post(pygame.event.Event(VERMELHO_ACERTADO))
            fogos_azul.remove(fogo)
        elif fogo.x < 0:
            fogos_azul.remove(fogo)

def ganhador_escrever(texto):
    ganhador_render = GANHADOR_FONTE.render(texto,1, BRANCO)
    JAN.blit(ganhador_render,
                  (LARGURA//2 - (ganhador_render.get_width()//2) ,
                  ALTURA//2 - ganhador_render.get_height()//2 ) )
    pygame.display.update()
    pygame.time.delay(3000)


def main():   
    vermelho = pygame.Rect(100, 300, GATO_ALTURA, GATO_LARGURA)
    azul = pygame.Rect(700, 300, GATO_ALTURA, GATO_LARGURA)

    largura_vermelho, altura_vermelho = 18,9
    largura_azul, altura_azul = 22, 11

    fogos_vermelho = []
    fogos_azul = []

    vida_vermelho = 7
    vida_azul = 7

    clock = pygame.time.Clock()
    rodar = True
    while rodar:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    rodar = False
                    pygame.quit()
 

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(fogos_vermelho) < MAX_FOGO:
                    fogo = pygame.Rect(vermelho.x + vermelho.width, 
                                       vermelho.y + vermelho.height//2 -2,
                                       largura_vermelho, altura_vermelho)
                    fogos_vermelho.append(fogo)
                    SOM_FOGO_TIRO.play()


                if event.key == pygame.K_RCTRL and len(fogos_azul) < MAX_FOGO:
                    fogo = pygame.Rect(azul.x, 
                                       azul.y + azul.height//2 -2,
                                       largura_azul,altura_azul)
                    fogos_azul.append(fogo)
                    SOM_FOGO_TIRO.play()

            if event.type == VERMELHO_ACERTADO:
                vida_vermelho -= 1
                SOM_FOGO_BOOM.play()
        
            if event.type == AZUL_ACERTADO:
                vida_azul -= 1
                SOM_FOGO_BOOM.play()

        texto_ganhador =""
        if vida_azul <= 0:
            texto_ganhador = "Vermelho Ganhou! Miauuuuu!"

        if vida_vermelho <= 0:
            texto_ganhador = "Azul Ganhou! Miauuuuu!"

        if texto_ganhador != "":
            desenhar_janela(vermelho, azul, fogos_vermelho, fogos_azul, vida_vermelho, vida_azul)
            ganhador_escrever(texto_ganhador)
            break

        tecla_pressionada = pygame.key.get_pressed()
        movimentar_vermelho(tecla_pressionada, vermelho)
        movimentar_azul(tecla_pressionada, azul)

        controlhe_fogo(fogos_vermelho, fogos_azul, vermelho, azul)



        desenhar_janela(vermelho, azul, fogos_vermelho, fogos_azul, vida_vermelho, vida_azul)
       


    main()




if __name__ == "__main__":
    main()
