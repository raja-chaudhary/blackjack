
import random
import os
from art import logo


def deal_card():
    '''Returns a random card from the deck.'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw!!"
    elif computer_score == 0:
        return "Computer has a Blackjack, Computer Wins!"
    elif user_score == 0:
        return "You Win, you had a Blackjack"
    elif user_score > 21:
        return "You Lose! You went over 21.."
    elif computer_score > 21:
        return "You Win! The opponent went over 21.."
    elif user_score > computer_score:
        return "You Win!"
    else:
        return "You Lose"


def play_game():

    print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"  User cards: {user_cards} with total score of {user_score}")
        print(f"  Dealer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input(
                "Press 'y' to deal another card or press 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"    Your final hand: {user_cards} and final score: {user_score}")
    print(
        f"    Computer's final hand: {computer_cards} and final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play Blackjack. Press y/n: ") == "y":
    os.system('clear')
    play_game()
