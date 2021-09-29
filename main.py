import pygame
import os

pygame.init()

WIDTH, HEIGHT = 1200, 800
CARD_WIDTH , CARD_HEIGHT = 150, 200
BUTTON_WIDTH, BUTTON_HEIGHT = 80, 80
FPS = 60
GREEN = (0,100,0)
BLACK = (0,0,0)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BlackJack")

font = pygame.font.Font('freesansbold.ttf', 26)

dealer_text = font.render("Dealer", True, BLACK)
player_text = font.render("Player", True, BLACK)

hit_image = pygame.transform.scale(pygame.image.load(os.path.join("Assets/options", "hit.png")),
                                   (BUTTON_WIDTH, BUTTON_HEIGHT))
stand_image = pygame.transform.scale(pygame.image.load(os.path.join("Assets/options", "stand.png")),
                                     (BUTTON_WIDTH, BUTTON_HEIGHT))


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

    sum_hand = hand_value(cards)

    return [player_cards, sum_hand]


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


def hand_value(cards):
    cards_sum = 0
    ace = False

    for card in cards:
        if card[1] == "jack" or card[1] == "queen" or card[1] == "king":
            cards_sum += 10
        elif card[1] == "ace":
            ace = True
            cards_sum += 1
        else:
            cards_sum += int(card[1])
        
    if ace and cards_sum + 10 <= 21:
        cards_sum += 10


    return cards_sum


def draw_window(player_cards,computer_cards, players_sum):
    players_sum_text = font.render("Your total sum is: "+str(players_sum), True, BLACK)

    step = 150

    WIN.fill(GREEN)
    WIN.blit(dealer_text, (0,100))
    WIN.blit(player_text, (0, 700))
    for card in player_cards:
        
        WIN.blit(card, (step + CARD_WIDTH,600))
        step += 150

    step = 150
    for card in computer_cards:
        
        WIN.blit(card, (step + CARD_WIDTH,0))
        step += 150
    
    WIN.blit(players_sum_text, (0,750))

    #pygame.display.update()


def draw_buttons():
    WIN.blit(hit_image, (300, 500))
    WIN.blit(stand_image, (390, 500))



def main():
    clock = pygame.time.Clock()
    run = True

    players_sum = 0

    player_cards, players_sum = player()
    computer_cards = computer()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window(player_cards, computer_cards, players_sum)
        draw_buttons()
        pygame.display.update()


    pygame.quit()


if __name__ == '__main__':
    main()





