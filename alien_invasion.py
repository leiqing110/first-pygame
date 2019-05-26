import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    #bg_color = (230,230,230)
    #程序框标题
    pygame.display.set_caption("外星人入侵")
    #创建一艘飞船
    ship = Ship(ai_settings,screen)
    #开始游戏的主循环
    while True:

        #监视键盘和鼠标事件
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()
        gf.check_events(ship)
        #每次循环都重新绘制屏幕
        ship.update()
        gf.update_screen(ai_settings, screen, ship)

run_game()