import pygame

pygame.init()

pantalla  = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Titulo')

dt = 0
clock = pygame.time.Clock()
running = True
p_pos = pygame.Vector2(pantalla.get_width()/2, pantalla.get_height()/2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pantalla.fill('white')

    pygame.draw.circle(pantalla, 'green', p_pos, 30)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        p_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        p_pos.y += 300 * dt
    if keys[pygame.K_a]:
        p_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        p_pos.x += 300 * dt

    pygame.display.flip()
    dt = clock.tick(60) / 800

pygame.quit()
