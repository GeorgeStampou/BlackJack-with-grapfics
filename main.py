import pygame
import os

pygame.init()

WIDTH, HEIGHT = 1200, 800
CARD_WIDTH , CARD_HEIGHT = 150, 200
FPS = 60
GREEN = (0,100,0)
BLACK = (0,0,0)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BlackJack")

font = pygame.font.Font('freesansbold.ttf', 32)

dealer_text = font.render("Dealer", True, BLACK)
player_text = font.render("Player", True, BLACK)



kind = {"heart", "diamond", "spade", "club"}
number = {"ace", 2, 3, 4, 5, 6, 7, 8, 9, 10,"jack", "queen", "king"}

deck = {(k,n) for k in kind for n in number}


def player(player_cards):
    print("\n******Player's turn!******")

    for _ in range(2):
        card = deck.pop()
        print(card)
        player_cards.add(card)

    print(f"\nPlayer's cards: {player_cards}")

    #sum_hand = hand_value(player_cards)


def draw_window(card):
    WIN.fill(GREEN)
    WIN.blit(dealer_text, (100,100))
    WIN.blit(player_text, (100, 700))
    WIN.blit(card, (300,0))
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    card = pygame.transform.scale(pygame.image.load(os.path.join("Assets/hearts", "ace_hearts.png")),
                                  (CARD_WIDTH, CARD_HEIGHT))
    player_cards = set()
    player(player_cards)

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window(card)

    pygame.quit()

if __name__ == '__main__':
    main()





