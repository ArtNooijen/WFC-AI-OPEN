
import pygame
pygame.init()
from grid import Grid
from tile import Tile

font = pygame.font.Font("./assets/custom_fonts/Poppins/Poppins-Light.ttf", 16)

width = 1200
height = 1200
rez = 30
display = pygame.display.set_mode((width, height))

def load_image(path, rez_, padding = 0):
    img = pygame.image.load(path).convert_alpha()
    img = pygame.transform.scale(img, (rez_ - padding, rez_ - padding))
    return img


def disp_msg(text, x, y):
    msg = font.render(str(text), 1, (255, 255, 255))
    display.blit(msg, (x, y))

def hover(mouse_pos, rez, grid):
    mx, my = mouse_pos
    x = mx // rez
    y = my // rez
    cell = grid.grid[y][x]
    cell_entropy = cell.entropy()
    cell_collpased = cell.collapsed
    cell_options = [opt.edges for opt in cell.options]
    pygame.draw.rect(display, (20, 20, 20), (mouse_pos[0], mouse_pos[1], 200, 100))
    disp_msg(f"entrophy  : {cell_entropy}", mx + 10, my + 10)
    disp_msg(f"collapsed : {cell_collpased}", mx + 10, my + 30)
    disp_msg(f"options   : {cell_options}", mx + 10, my + 50)


def main():
    
    options = []
    edge_options = []
    for i in range(5):
        
        #img = load_image(f"./assets/{i}.png", rez)
        img = load_image(f"./tiles/circuit/{i}.png", rez)
        
        # load corner tile
        #img = load_image(f"./assets/c{i}.png", rez)
        options.append(Tile(img))
    # for i in range(5):
    
    #     img = load_image(f"./assets/c{i}.png", rez)
    #     edge_options.append(Tile(img))

    # edge conditions for tetris tiles
    options[0].edges = [0, 0, 0, 0]
    options[1].edges = [1, 1, 0, 1]
    options[2].edges = [1, 1, 1, 0]
    options[3].edges = [0, 1, 1, 1]
    options[4].edges = [1, 0, 1, 1]

    # edge conditions for corner tiles
    # edge_options[0].edges = [0, 0, 0, 0]
    # edge_options[1].edges = [1, 1, 0, 0]
    # edge_options[2].edges = [0, 1, 1, 0]
    # edge_options[3].edges = [0, 0, 1, 1]
    # edge_options[4].edges = [1, 0, 0, 1]

    # update tile rules for each tile
    for i, tile in enumerate(options):
        tile.index = i 
        tile.set_rules(options)
        

    # wave grid
    wave = Grid(width, height, rez, options)
    wave.initiate()


    hover_toggle = True

    # game loop
    loop = True
    while loop:

        display.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    hover_toggle = not hover_toggle

                if event.key == pygame.K_q:
                    loop = False
                    exit()
            
        wave.draw(display)
        wave.collapse()

        
        if hover_toggle:
            mos_pos = pygame.mouse.get_pos()
            hover(mos_pos, rez, wave)


        pygame.display.flip()


if __name__ == "__main__":
    main()

