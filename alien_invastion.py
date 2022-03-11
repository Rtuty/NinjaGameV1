import sys
import pygame
from settings import *
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien

def run_game():
    pygame.init()
    ai_settings = Settings()
    bullets = Group()
    aliens = Group()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height), pygame.RESIZABLE)
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings, screen)
    gf.create_fleet(ai_settings, screen, ship, aliens)
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
        gf.update_aliens(ai_settings, aliens)


run_game()
