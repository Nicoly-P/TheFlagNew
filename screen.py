for bush in range(cs.NUM_OF_BUSHES):
    random_bush_x = random.randint(0,997)
    random_bush_y = random.randint(0,497)
    display_surface.blit(cs.BUSH, (random_bush_x, random_bush_y))
    pygame.display.flip()
    pygame.display.update()
