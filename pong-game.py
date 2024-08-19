import pygame
import sys

# Inicializar o pygame
pygame.init()

# Configurações da tela
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pong')

# Cores
black = (0, 0, 0)
white = (255, 255, 255)

# Configurações da raquete
paddle_width, paddle_height = 10, 100
paddle_speed = 10

# Configurações da bola
ball_width = 15

# Função para desenhar a raquete
def draw_paddle(x, y):
    pygame.draw.rect(screen, white, pygame.Rect(x, y, paddle_width, paddle_height))

# Função para desenhar a bola
def draw_ball(x, y):
    pygame.draw.ellipse(screen, white, pygame.Rect(x, y, ball_width, ball_width))

# Função principal do jogo
def main():
    # Inicializar as posições e velocidades
    paddle1_x, paddle1_y = 30, (height - paddle_height) / 2
    paddle2_x, paddle2_y = width - 30 - paddle_width, (height - paddle_height) / 2
    ball_x, ball_y = (width - ball_width) / 2, (height - ball_width) / 2
    ball_speed_x, ball_speed_y = 7, 7  # Inicializar a velocidade da bola

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Movimentação das raquetes
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and paddle1_y > 0:
            paddle1_y -= paddle_speed
        if keys[pygame.K_s] and paddle1_y < height - paddle_height:
            paddle1_y += paddle_speed
        if keys[pygame.K_UP] and paddle2_y > 0:
            paddle2_y -= paddle_speed
        if keys[pygame.K_DOWN] and paddle2_y < height - paddle_height:
            paddle2_y += paddle_speed

        # Movimentação da bola
        ball_x += ball_speed_x
        ball_y += ball_speed_y

        # Colisões com as bordas
        if ball_y <= 0 or ball_y >= height - ball_width:
            ball_speed_y *= -1
        if ball_x <= 0 or ball_x >= width - ball_width:
            ball_speed_x *= -1

        # Colisões com as raquetes
        if (paddle1_x < ball_x < paddle1_x + paddle_width and
                paddle1_y < ball_y < paddle1_y + paddle_height) or \
           (paddle2_x < ball_x < paddle2_x + paddle_width and
                paddle2_y < ball_y < paddle2_y + paddle_height):
            ball_speed_x *= -1

        # Limpar a tela
        screen.fill(black)

        # Desenhar a raquete e a bola
        draw_paddle(paddle1_x, paddle1_y)
        draw_paddle(paddle2_x, paddle2_y)
        draw_ball(ball_x, ball_y)

        # Atualizar a tela
        pygame.display.flip()

        # Controlar a taxa de quadros
        pygame.time.Clock().tick(60)

if __name__ == "__main__":
    main()
