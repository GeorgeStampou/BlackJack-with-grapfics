import pygame
import os

pygame.init()
pygame.font.init()


class Button:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        an_action = False
        pos = pygame.mouse.get_pos()
        # check if mouse over buttons and if the buttons are left-clicked
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                an_action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        surface.blit(self.image, (self.rect.x, self.rect.y))
        return an_action


WIDTH, HEIGHT = 1200, 800
CARD_WIDTH, CARD_HEIGHT = 150, 200
BUTTON_WIDTH, BUTTON_HEIGHT = 80, 80
RESTART_WIDTH, RESTART_HEIGHT = 150, 50

FPS = 60
GREEN = (0, 100, 0)
BLACK = (0, 0, 0)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BlackJack")

font = pygame.font.SysFont("Sans", 26)

dealer_text = font.render("Dealer", True, BLACK)
player_text = font.render("Player", True, BLACK)

hit_image = pygame.transform.scale(pygame.image.load(os.path.join("Assets/options", "hit.png")),
                                   (BUTTON_WIDTH, BUTTON_HEIGHT))
stand_image = pygame.transform.scale(pygame.image.load(os.path.join("Assets/options", "stand.png")),
                                     (BUTTON_WIDTH, BUTTON_HEIGHT))
restart_image = pygame.transform.scale(pygame.image.load(os.path.join("Assets/options", "restart.png")),
                                       (RESTART_WIDTH, RESTART_HEIGHT))
play_again_image = pygame.transform.scale(pygame.image.load(os.path.join("Assets/options", "playagain.png")),
                                          (RESTART_WIDTH, RESTART_HEIGHT))

kind = {"heart", "diamond", "spade", "club"}
number = {"ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king"}

deck = {(k, n) for k in kind for n in number}


def new_card(pcards, value_of_cards):
    card = deck.pop()
    print(card)
    value_of_cards.add(card)
    print("Assets/" + card[0], str(card[1]) + "_" + card[0] + ".png")

    card_image = pygame.transform.scale(pygame.image.load(os.path.join("Assets/" + card[0],
                                                                       str(card[1]) + "_" + card[0] + ".png")),
                                        (CARD_WIDTH, CARD_HEIGHT))
    pcards.add(card_image)
    return [pcards, value_of_cards]


def player():
    print("\n******Player's turn!******")
    player_cards = set()
    cards = set()

    for _ in range(2):
        new_card(player_cards, cards)
    print(f"\nPlayer's cards: {player_cards}")

    return [player_cards, cards]


def computer():
    computer_cards = set()
    cards = set()

    print("\n******Computer's turn!******")
    new_card(computer_cards, cards)

    print(f"\nComputer's cards: {cards}")

    return [computer_cards, cards]


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


def draw_window():
    WIN.fill(GREEN)
    WIN.blit(dealer_text, (0, 100))
    WIN.blit(player_text, (0, 700))

    # pygame.display.update()


def draw_cards(player_cards, computer_cards):
    step = 150
    for card in player_cards:
        WIN.blit(card, (step + CARD_WIDTH, 600))
        step += 150

    step = 150
    for card in computer_cards:
        WIN.blit(card, (step + CARD_WIDTH, 0))
        step += 150


def draw_cards_sum(players_sum, computers_sum):
    players_sum_text = font.render("Your total sum is: " + str(players_sum), True, BLACK)
    computers_sum_text = font.render("Dealer's sum is: " + str(computers_sum), True, BLACK)
    WIN.blit(players_sum_text, (0, 750))
    WIN.blit(computers_sum_text, (0, 150))


def check_round(players_sum, computers_sum, scores):
    if players_sum == 21:
        scores[0] += 1
        draw_result("***CONGRATULATIONS***. You won the round!!!", scores)
    elif players_sum > 21:
        scores[1] += 1
        draw_result("***You lost***", scores)

    else:
        if computers_sum > 21:
            # draw_result("Computer is out.")
            scores[0] += 1
            draw_result("***CONGRATULATIONS***. You won the round!!!", scores)

        else:
            if computers_sum > players_sum:
                scores[1] += 1
                draw_result("Computer won!", scores)

            if computers_sum == players_sum:
                draw_result("Deuce.", scores)

    return scores


# kane mazi sthn draw result to string kai to score
def draw_result(string, scores):
    string_text = font.render(string, True, BLACK)
    scores_text = font.render("***SCORE*** You: " + str(scores[0]) + " Dealer: " + str(scores[1]), True, BLACK)
    string_rect = string_text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
    scores_rect = scores_text.get_rect(center=(WIDTH / 2, (HEIGHT / 2) + 50))
    WIN.blit(string_text, string_rect)
    # scores den vgainei swsta opote comment
    # WIN.blit(scores_text, scores_rect)


def main(scores, rounds):
    clock = pygame.time.Clock()
    run = True

    hit_button = Button(300, 500, hit_image, 1)
    stand_button = Button(390, 500, stand_image, 1)
    restart_button = Button(1000, 400, restart_image, 1)
    play_again_button = Button(1000, 520, play_again_image, 1)

    player_cards, values_pcards = player()
    players_sum = hand_value(values_pcards)
    computer_cards, values_ccards = computer()
    computers_sum = hand_value(values_ccards)

    while run:

        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()
        draw_cards(player_cards, computer_cards)
        draw_cards_sum(players_sum, computers_sum)

        if stand_button.draw(WIN):
            print("STAND")
            flag = True
            while flag:
                if computers_sum < players_sum:
                    new_card(computer_cards, values_ccards)
                    computers_sum = hand_value(values_ccards)
                else:
                    flag = False
        if hit_button.draw(WIN):
            print("HIT")
            new_card(player_cards, values_pcards)
            players_sum = hand_value(values_pcards)

        if computers_sum != 0:
            scores = check_round(players_sum, computers_sum, scores)

            # if scores != [0, 0]:

            if play_again_button.draw(WIN):
                print("play again")
                # scores += scores
                # rounds += 1
                for card in values_pcards:
                    deck.add(card)

                for card in values_ccards:
                    deck.add(card)
                print(len(deck))
                main(scores, rounds)
                '''
                if restart_button.draw(WIN):
                    print("restart")
                    main(scores, rounds)
                '''

        else:
            print("ERROR! Computer has no score.")

        pygame.display.update()

    print(len(deck))
    print("\n******Score******")
    print(f"\nPlayer's score: {scores[0]} - Computer's score: {scores[1]}")

    for card in player_cards:
        deck.add(card)

    for card in computer_cards:
        deck.add(card)

    pygame.quit()


if __name__ == '__main__':
    scores = [0, 0]
    rounds = 0
    main(scores, rounds)
