from utils import Card, Deck, Player
from simple_bot import Bot

# Create a deck of cards


deck = Deck(1)

# Create a player
dealer = Player()
player = Player()

bot = Bot()
bot.capital = 1000

def simulate_round(bot):
    global deck, player, dealer
    if len(deck) < 20: deck = Deck(1)
    bet = bot.bet(deck)
    
    player.add(deck.draw(2))
    dealer.add(deck.draw(2))
    while player.get_hand_value() < 21:
        action = bot.turn(player)
        print(action)
        if action == "Hit":
            player.add(deck.draw())
        elif action == "Stand" or player.get_hand_value() >= 21:
            break
    
    while dealer.get_hand_value() < 17:
        dealer.add(deck.draw())
    
    if player.get_hand_value() > 21 and dealer.get_hand_value() > 21:
        player.clear_hand()
        dealer.clear_hand()
        return "Tie"
    elif player.get_hand_value() > 21:
        player.clear_hand()
        dealer.clear_hand()
        bot.capital -= bet
        return "Dealer"
    elif dealer.get_hand_value() > 21:
        player.clear_hand()
        dealer.clear_hand()
        bot.capital += bet
        return "Player"
    elif player.get_hand_value() > dealer.get_hand_value():
        player.clear_hand()
        dealer.clear_hand()
        bot.capital += bet
        return "Player"
    elif player.get_hand_value() < dealer.get_hand_value():
        player.clear_hand()
        dealer.clear_hand()
        bot.capital -= bet
        return "Dealer"
    else:
        return "Tie"

def simulate(bot, rounds_to_simulate):
    capital_changes = []
    rounds = 0
    player_wins = 0
    dealer_wins = 0
    ties = 0

    while bot.capital > 0 and rounds < rounds_to_simulate:
        capital_changes.append(bot.capital)
        result = simulate_round(bot)
        rounds += 1
        if result == "Player":
            player_wins += 1
        elif result == "Dealer":
            dealer_wins += 1
        else:
            ties += 1

    return capital_changes, rounds, player_wins, dealer_wins, ties

import matplotlib.pyplot as plt

capital_changes, rounds, player_wins, dealer_wins, ties = simulate(bot, 1000000)
plt.plot(capital_changes)
plt.show()
print(f"Player wins: {player_wins}")
print(f"Dealer wins: {dealer_wins}")
print(f"Ties: {ties}")
print(f"Rounds: {rounds}")


