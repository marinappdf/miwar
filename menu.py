import pygame
import sys
import os
import subprocess

pygame.init()

LARGURA, ALTURA = 800, 600
JAN = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Menu Principal")

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
AZUL = (0 , 0, 255)

FONTE_MENU = pygame.font.SysFont('comicsans', 40)
FUNDO = pygame.transform.scale(pygame.image.load(os.path.join('Recursos', 'fundo.png')), (LARGURA, ALTURA))

def desenhar_menu(selecao):
    JAN.blit(FUNDO, (0,0))
    
    opcoes = ['Jogar', 'Sair']
    
    for i, opcao in enumerate(opcoes):
        if i == selecao:
            texto = FONTE_MENU.render(opcao, True, AZUL)
        else:
            texto = FONTE_MENU.render(opcao, True, VERMELHO)
        
        JAN.blit(texto, (LARGURA//2 - texto.get_width()//2, ALTURA//2 - 100 + i*60))
        
    pygame.display.update()

def menu():
    selecao = 0
    rodando = True
    
    while rodando:
        desenhar_menu(selecao)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
      
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selecao += 1
                    if selecao > 1:  
                        selecao = 0
                elif event.key == pygame.K_UP:
                    selecao -= 1
                    if selecao < 0:  
                        selecao = 1
                
                if event.key == pygame.K_RETURN:
                    if selecao == 0: 
                        print("Iniciando o jogo...")
                        subprocess.run(["python3", "batalha.py"])
                    elif selecao == 1:
                        pygame.quit()
                        sys.exit()
        
        pygame.display.update()

if __name__ == "__main__":
    menu()
