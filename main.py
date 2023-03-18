import sys
from objects import *
from carddeck import *
pygame.init()
clock = pygame.time.Clock()
frame = 0

screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

# Создание колоды с картами
cardDeck = []
for key in mydeck:
    cardDeck.append(Card(screen, 600, 600, mydeck[key]['Фракция'], key, mydeck[key]['Сила'], mydeck[key]['Мана'], mydeck[key]['Действие']))
print(len(cardDeck))

while True:
    screen.fill('White')
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()

    for item in cardDeck:
        item.draw()

    pygame.display.update()
    frame += 1
    clock.tick(2)