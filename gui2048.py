# gui2048

# FULL CONTROLS:
# 


import pygame
import logic2048
import random
import math
class GUI2048:
    def __init__(self):
        self._running = True
        self._game = logic2048.Logic2048()
        self._surface = pygame.display.get_surface()
        self._game_over = False

    def run(self) -> None:
        """
        Main loop for running the game
        Initialized and runs pygame and then quits it
        """
        pygame.init()

        self._resize_surface((600, 600))
        self._surface = pygame.display.get_surface()
        clock = pygame.time.Clock()
        self._game.spawn()
        self._game.spawn()
        #self._game.set_board([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,1024,1024]])
        """
        while self._running:
                clock.tick(30)
                if not self._game_over:
                    self._handle_events()
                else:
                    self._handle_exit()
                self._redraw()
                
        """
        try: 
            while self._running:
                clock.tick(30)
                if not self._game_over:
                    self._handle_events()
                else:
                    self._handle_exit()
                self._redraw()
        except Exception as e:
            print(e)
        finally:
            pygame.quit()
        
        
    def _resize_surface(self, size: tuple[int, int]) -> None:
        """
        Resizes the surface
        """
        pygame.display.set_mode(size, pygame.RESIZABLE)


    def _handle_events(self) -> None:
        """
        Does actions based on the users events
        Also ticks every 30 frames aka 1 second
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._end_game()
            elif event.type == pygame.VIDEORESIZE:
                self._resize_surface(event.size)
                self._surface = pygame.display.get_surface()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self._game.left()
                    self._game_over = self._game.spawn()
                if event.key == pygame.K_RIGHT:
                    self._game.right()
                    self._game_over = self._game.spawn()
                if event.key == pygame.K_UP:
                    self._game.up()
                    self._game_over = self._game.spawn()
                if event.key == pygame.K_DOWN:
                    self._game.down() 
                    self._game_over = self._game.spawn()             
        
        
    def _redraw(self) -> None:
        """
        Draws the field, changes based on state of the game
        """
        width = self._surface.get_width()
        height = self._surface.get_height()
        corner_x = width/6 
        corner_y = height/6 
        if self._game_over:
            self._surface.fill(pygame.Color(255, 150, 150))
        else:
            self._surface.fill(pygame.Color(250, 248, 241))

        pygame.draw.rect(self._surface, pygame.Color(152, 137, 122), pygame.Rect(corner_x-5, corner_y-5, width/6*4+5, height/6*4 +5))
        board = self._game.get_board()
        for i in range(len(board)):
            for j in range(len(board[i])):
                self._draw_num(board[i][j], j, i, {'x':corner_x,'y':corner_y})

        if self._game_over:
            font = pygame.font.Font(None,size=30)
            text_surface = font.render('Q to quit', False, (0, 0, 0))
            text_rect = text_surface.get_rect(center=(width/2, height/15*14.5))
            self._surface.blit(text_surface, text_rect)
        #self.draw_rounded_rect(self._surface, pygame.Color(0,0,0), pygame.Rect(100,100,400,400),20)
        pygame.display.flip()

    def _draw_num(self, num: int, x: int, y: int, corner: dict) -> None:
        """
        Draws a jewel at a specfic x and y
        """
        width = self._surface.get_width()
        height = self._surface.get_height()

        pixel_width = width / 6
        pixel_height = height / 6
        if num == 0:
            color = pygame.Color(186, 173, 154)
        elif num == 2:
            color = pygame.Color(237, 229, 229)
        elif num == 4:
            color = pygame.Color(224, 210, 180)
        elif num == 8:
            color = pygame.Color(231, 117, 124)
        elif num == 16:
            color = pygame.Color(217, 143, 100)
        elif num == 32:
            color = pygame.Color(222, 129, 102)
        elif num == 64:
            color = pygame.Color(224, 108, 77)
        elif num == 128:
            color = pygame.Color(229, 205, 121)
        elif num == 256:
            color = pygame.Color(230, 204, 115)
        elif num == 512:
            color = pygame.Color(233, 207, 111)
        elif num == 1024:
            color = pygame.Color(230, 202, 95)
        else:
            color = pygame.Color(0, 0, 0)

        self.draw_rounded_rect(self._surface, color, pygame.Rect(
            corner['x'] + x * pixel_width, corner['y'] + y * pixel_height,
            pixel_width-5, pixel_height-5),10)
        if num != 0:
            if num < 1000:
                font = pygame.font.Font(None,int(height/6)-25)
            else:
                font = pygame.font.Font(None,int(height/10)-15)
            if num == 2 or num == 4:
                text_surface = font.render(str(num), False, (114, 101, 84))
            else:
                text_surface = font.render(str(num), False, (255, 255, 255))
            text_rect = text_surface.get_rect(center = (corner['x'] + x * pixel_width + (pixel_width-5) / 2, corner['y'] + y * pixel_height + (pixel_height-5)/2))
            self._surface.blit(text_surface, text_rect)

    def _end_game(self) -> None:
        """
        Ends the game
        """
        self._running = False

    def _handle_exit(self) -> None:
        """
        Handles user input after the game ends
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._end_game()
            elif event.type == pygame.VIDEORESIZE:
                self._resize_surface(event.size)
                self._surface = pygame.display.get_surface()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self._end_game()

    def draw_rounded_rect(self,surface, color, rect, radius):
        pygame.draw.rect(surface, color, pygame.Rect(rect.x + radius, rect.y, rect.width - 2 * radius, rect.height))
        pygame.draw.rect(surface, color, pygame.Rect(rect.x, rect.y + radius, rect.width, rect.height - 2 * radius))
        pygame.draw.rect(surface, color, pygame.Rect(rect.x, rect.y, rect.width, rect.height), 10, radius)


if __name__ == '__main__':
    GUI2048().run()


    
