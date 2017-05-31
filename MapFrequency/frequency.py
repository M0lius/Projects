import sys
import math
import json

# Import a library of functions called 'pygame'
import pygame
size = 40;

# Define some colors
BLACK = (0, 0, 0)
GREY = (200,200,200)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0,0,255)
RED = (255, 0, 0)
BROWN = (160,82,45)


# Used to manage how fast the screen updates
clock = pygame.time.Clock()

def offSet(a):
    return a + math.ceil((size+1)/2);

def drawRoad(screen,x,y,xP,yP):
    pygame.draw.line(screen, BLACK,
     [x, y], [xP, yP], 1);
    return;

def main():

    #Check Arguments
    if len(sys.argv)!= 2:
        print("Incorrent Number Arguments");
        return;
    print("\nGOT MAP: " + sys.argv[1]);

    #Get Map JSON
    map = json.loads(open(sys.argv[1]).read());
    print ("NAME : " + map["name"]);

    # Initialize the game engine
    dimensions = (size*(int(map["width"]) + 2), size*(int(map["height"]) + 2));
    screen = pygame.display.set_mode(dimensions);
    pygame.display.set_caption(map["name"] + "'s Board Graph");

    pygame.font.init() # you have to call this at the start,
    myfont = pygame.font.SysFont('Comic Sans MS', math.ceil(2*size/3))

    pygame.init()



    # -------- Main Program Loop -----------
    width = int(map["width"]);
    height = int(map["height"]);
    bottom = size*(height + 2)
    right = size*(width + 2)
    done = False;
    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # --- Game logic should go here

        # --- Screen-clearing code goes here

        # Here, we clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.

        # If you want a background image, replace this clear with blit'ing the
        # background image.
        screen.fill(WHITE)

        # --- Drawing code should go here
            # HORIZONTAL LINES = 1 more than boxes
        for x in range(width + 1):
            pos = (x+1)*size
            pygame.draw.line(screen, GREY , [pos, size], [pos,bottom - size], 1)
            #X-Coordinates
            if x != width:
                txt = myfont.render(str(x), False, BLACK);
                screen.blit(txt,(pos + math.ceil(size/4),math.ceil(size/2)))

            # VERTICAL LINES = 1 more than boxes
        for y in range(height + 1):
            pos = (y+1)*size
            pygame.draw.line(screen, GREY , [size, pos], [right - size,pos], 1)
            #Y-Coordinates
            if y != height:
                txt = myfont.render(str(y), False, BLACK);
                screen.blit(txt,(math.ceil(size/3), pos + math.ceil(size/4)))

            #DRAW EDGES FIRST - FIND NODES in Graph
        for node in map["nodes"]:
            x = int(node["x"]) + 1;
            y = int(node["y"]) + 1;

            #START edge
            if node["index"] == "0":
                drawRoad(screen,offSet(x*size),offSet(y*size),
                    offSet(size*(width)),offSet(size*(height)));

            #EDGES in NODE
            for edge in node["edges"]:
                nodeP = map["nodes"][int(edge)];
                xP = int(nodeP["x"]) + 1;
                yP = int(nodeP["y"]) + 1;
                drawRoad(screen,offSet(x*size),offSet(y*size),
                    offSet(xP*size),offSet(yP*size));

            #DRAW NODES NOW
        for node in map["nodes"]:
            x = int(node["x"]) + 1;
            y = int(node["y"]) + 1;
            COLOR = RED;

            if(node["type"] == "B"):
                COLOR = BLUE;
            elif(node["type"] == "G"):
                COLOR = GREEN;

            pygame.draw.circle(screen, COLOR, (offSet(size*x), offSet(size*y)),
            math.ceil(size/3), 0);

            #DRAW OBJECTS
            #---START
            pygame.draw.rect(screen,BROWN,
            (offSet(size*(width - 1)), offSet(size*(height - 1)),size*2,size*2))

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)

    # Close the window and quit.
    pygame.quit()

    #FINISHED INFO
    print("\n FINISHED! \n");

if __name__ == "__main__":
    main()
