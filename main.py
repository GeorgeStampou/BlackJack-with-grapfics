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


def player():
    print("\n******Player's turn!******")
    player_cards = set()
    cards = set()

    for _ in range(2):
        card = deck.pop()
        print(card)
        cards.add(card)
        print("Assets/"+card[0], str(card[1]) + "_" + card[0]+".png")

        card_image = pygame.transform.scale(pygame.image.load(os.path.join("Assets/"+card[0], str(card[1]) + "_" + card[0]+".png")),
                                      (CARD_WIDTH, CARD_HEIGHT))
        player_cards.add(card_image)

    print(f"\nPlayer's cards: {cards}")

    #sum_hand = hand_value(player_cards)

    return player_cards


def computer():
    computer_cards = set()
    cards = set()

    print("\n******Computer's turn!******")

    for _ in range(2):
        card = deck.pop()
        print(card)
        cards.add(card)
        print("Assets/"+card[0], str(card[1]) + "_" + card[0]+".png")

        card_image = pygame.transform.scale(pygame.image.load(os.path.join("Assets/"+card[0], str(card[1]) + "_" + card[0]+".png")),
                                      (CARD_WIDTH, CARD_HEIGHT))
        computer_cards.add(card_image)

    print(f"\nComputer's cards: {cards}")

    return computer_cards


def draw_window(player_cards,computer_cards):

    step = 150

    WIN.fill(GREEN)
    WIN.blit(dealer_text, (100,100))
    WIN.blit(player_text, (100, 700))
    for card in player_cards:
        
        WIN.blit(card, (step + CARD_WIDTH,600))
        step += 150

    step = 150
    for card in computer_cards:
        
        WIN.blit(card, (step + CARD_WIDTH,0))
        step += 150
        
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True


    player_cards = player()
    computer_cards = computer()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window(player_cards,computer_cards)

    pygame.quit()

if __name__ == '__main__':
    main()





