

from datetime import datetime
import sys
import pygame

from codegame.const import COLOR_MENU, COLOR_TITLE, MENU_OPTION, SCORE_POS
from codegame.DBProxy import DBProxy


class Score:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/img/ScoreBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0,top=0)

    def save_score(self, menu_option, player_score: list[int]):
        pygame.mixer.music.load('./assets/bgmusic.mp3')
        pygame.mixer.music.play(loops=-1, start=1.5, fade_ms=0)
        pygame.mixer.music.set_volume(0.3)
        text = 'Enter your name (4 characteres):'
        db_proxy = DBProxy('DBScore')
        name = ''
        score = player_score[0]
        
        while True:

            self.window.fill((0, 0, 0))

            self.window.blit(source=self.surf, dest=self.rect)
            
            self.score_text(80, f'VICTORY!!', COLOR_MENU, SCORE_POS['Title'] )
            self.score_text(30, text, COLOR_MENU, SCORE_POS['EnterName'] ) 
            

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() # fechar janela
                    sys.exit() # fechar jogo  
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and len(name) == 4:
                        db_proxy.save({'name': name, 'score': score, 'date': get_formatted_date()})    
                        self.show_score()
                        return 
                    elif event.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 4:
                            name += event.unicode
            self.score_text(30, name, COLOR_MENU, SCORE_POS['Name'] ) 
            pygame.display.flip()

    def show_score(self):
        pygame.mixer.music.load('./assets/bgmusic.mp3')
        pygame.mixer.music.play(loops=-1, start=1.5, fade_ms=0)
        pygame.mixer.music.set_volume(0.3)
        self.window.blit(source= self.surf, dest= self.rect)
        self.score_text(80, f'TOP 10 SCORE', COLOR_TITLE, SCORE_POS['Title'] )
        self.score_text(45, f'NAME          SCORE                      DATE      ', COLOR_MENU, SCORE_POS['Label'] )
        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()

        for i in list_score:
            id_, name, score, date = i
            self.score_text(45, f'{name}        {score :05d}               {date}      ', COLOR_MENU, SCORE_POS[list_score.index(i)])

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() # fechar janela
                    sys.exit() # fechar jogo  
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return 
            pygame.display.flip()



    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font = pygame.font.Font("assets/fonts/Nosifer-Regular.ttf", text_size)
        text_surf: pygame.Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: pygame.Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

def get_formatted_date():
    current_datetime = datetime.now()
    current_date = current_datetime.strftime("%d/%m/%y")
    return f"{current_date}"