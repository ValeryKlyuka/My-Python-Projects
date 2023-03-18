import random
import pygame
pygame.init()

class Card:
    def __init__(self, screen, x, y, fraction, essence, strength, mana, ability):
        self.screen = screen
        self.x = x
        self.y = y
        self.strength = strength
        self.mana = mana
        self.ability = ability
        self.fraction = fraction
        self.essence = essence
        self.image = pygame.image.load(f'images/card/essences/{fraction}/{essence}.png')
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.text_back = pygame.image.load('images/card/text_back.png')
        self.font1 = pygame.font.Font('fonts/mr_izax_thin_izax.otf', 30)
        self.font2 = pygame.font.Font('fonts/mr_izax_thin_izax.otf', 18)
        if len(self.essence.split()) == 1:
            self.essence_render = [self.font1.render(self.essence.split()[0], True, 'White')]
            self.essence_render_rect = [self.essence_render[0].get_rect(center=(self.x, self.y + 70))]
        elif len(self.essence.split()) == 2:
            self.essence_render = [self.font1.render(f'{self.essence.split()[0]}', True, 'White'),
                                   self.font1.render(f'{self.essence.split()[1]}', True, 'White')]
            self.essence_render_rect = [self.essence_render[0].get_rect(center=(self.x, self.y + 70)),
                                        self.essence_render[1].get_rect(center=(self.x, self.y + 90))]
        self.ability_render = [self.font2.render(self.ability[0], True, 'White'),
                               self.font2.render(self.ability[1], True, 'White')]
        self.ability_render_rect = [self.ability_render[0].get_rect(center=(self.x, self.y + 116)),
                                    self.ability_render[1].get_rect(center=(self.x, self.y + 130))]
        self.fraction_icon = pygame.image.load(f'images/card/fraction_icons/{self.fraction}.png')
        self.strength_icon = pygame.image.load('images/card/strangth_frame.png')
        self.mana_icon = pygame.image.load('images/card/mana_frame.png')
        self.frame = pygame.image.load('images/card/frame.png')

        #self.frame = pygame.image.load('images/card/frame.png')
        #self.frame_rect = self.frame.get_rect(center=(self.x, self.y))
        #self.entity_image = pygame.image.load(f'images/entities/{self.entity}.png')
        #self.entity_rect = self.entity_image.get_rect(center=(self.x, self.y))
        #self.icon = pygame.image.load(f'images/card/{self.type[0]}.png')
        #self.icon_rect = self.icon.get_rect(center=(self.x, self.y))
        #self.force_frame = pygame.image.load('images/card/little_frame.png')
        #self.mana_frame = self.force_frame
        #self.force_frame_rect = self.force_frame.get_rect(center = (self.x + 60, self.y - 108))
        #self.mana_frame_rect = self.mana_frame.get_rect(center=(self.x - 60, self.y + 113))
        #self.title = self.font.render(f'{self.adj.capitalize()} {self.entity.lower()}', True, 'Black')
        #self.title_rect = self.title.get_rect(topleft=(self.x-85, self.y-120))
        #self.subtitle = self.font.render(f'{self.type[1]}', True, 'White')
        #self.subtitle_rect = self.subtitle.get_rect(center=(self.x, self.y + 62))
        #self.font_2 = pygame.font.Font('fonts/tupo-vyaz_regular.ttf', 40)
        #self.text_force = self.font_2.render(str(self.force), True, 'Black')
        #self.text_force_rect = self.text_force.get_rect(center=(self.x + 60, self.y - 108))
        #self.text_mana = self.font_2.render(str(self.mana), True, 'DeepSkyBlue')
        #self.text_mana_rect = self.text_mana.get_rect(center=(self.x - 60, self.y + 115))
        #self.font_3 = pygame.font.Font('fonts/tupo-vyaz_regular.ttf', 16)
        #self.text_ability = self.font_3.render(str(self.ability), True, 'Black')
        #self.text_ability_rect = self.text_ability.get_rect(bottomleft=(self.x - 20, self.y + 122))
        #self.flip_side = pygame.image.load('images/card/card_flip_side.png')
        #self.flip_side_rect = self.flip_side.get_rect(center=(self.x, self.y))
    def draw(self):
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.text_back, self.rect)
        for item in self.essence_render:
            self.screen.blit(item, self.essence_render_rect[self.essence_render.index(item)])
        for item in self.ability_render:
            self.screen.blit(item, self.ability_render_rect[self.ability_render.index(item)])
        self.screen.blit(self.fraction_icon, (self.x - 87, self.y - 137))
        self.screen.blit(self.strength_icon, (self.x - 77, self.y - 70))
        self.screen.blit(self.mana_icon, (self.x - 77, self.y - 23))
        self.screen.blit(self.frame, self.frame.get_rect(center=(self.x, self.y)))

        self.strength_render = self.font1.render(str(self.strength), True, 'White')
        self.strength_render_rect = self.strength_render.get_rect(center=(self.x - 57, self.y - 53))
        self.screen.blit(self.strength_render, self.strength_render_rect)

        self.mana_render = self.font1.render(str(self.mana), True, 'White')
        self.mana_render_rect = self.mana_render.get_rect(center=(self.x - 57, self.y - 6))
        self.screen.blit(self.mana_render, self.mana_render_rect)

        #self.screen.blit(self.entity_image, self.entity_rect)
        #self.screen.blit(self.icon, self.icon_rect)
        #self.screen.blit(self.force_frame, self.force_frame_rect)
        #self.screen.blit(self.mana_frame, self.mana_frame_rect)
        #self.screen.blit(self.title, self.title_rect)
        #self.screen.blit(self.subtitle, self.subtitle_rect)
        #self.screen.blit(self.text_force, self.text_force_rect)
        #self.screen.blit(self.text_mana, self.text_mana_rect)
        #self.screen.blit(self.text_ability, self.text_ability_rect)
        #self.screen.blit(self.flip_side, self.flip_side_rect)
