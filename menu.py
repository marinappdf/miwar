import pygame
import sys
import subprocess

# Inicializa o Pygame
pygame.init()

# Definir dimensões da janela
LARGURA, ALTURA = 800, 600
JAN = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Menu Principal")

# Definir cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)

# Definir fontes
FONTE_MENU = pygame.font.SysFont('comicsans', 40)

# Função para desenhar o menu
def desenhar_menu(selecao):
    JAN.fill(PRETO)
    
    # Opções do menu
    opcoes = ['Jogar', 'Sair']
    
    for i, opcao in enumerate(opcoes):
        if i == selecao:
            texto = FONTE_MENU.render(opcao, True, VERMELHO)
        else:
            texto = FONTE_MENU.render(opcao, True, BRANCO)
        
        # Centraliza o texto
        JAN.blit(texto, (LARGURA//2 - texto.get_width()//2, ALTURA//2 - 100 + i*60))
    
    pygame.display.update()

# Função principal
def menu():
    selecao = 0
    rodando = True
    
    while rodando:
        desenhar_menu(selecao)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # Navega no menu com as setas
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selecao += 1
                    if selecao > 2:  # Limite inferior
                        selecao = 0
                elif event.key == pygame.K_UP:
                    selecao -= 1
                    if selecao < 0:  # Limite superior
                        selecao = 2
                
                # Seleciona opção com Enter
                if event.key == pygame.K_RETURN:
                    if selecao == 0:  # Jogar
                        print("Iniciando o jogo...")
                        subprocess.run(["python3", "batalha.py"])
                        #rodando = False  # Aqui você pode iniciar o loop do jogo principal
                    elif selecao == 1:
                        pygame.quit()
                        sys.exit()
        
        pygame.display.update()

if __name__ == "__main__":
    menu()
