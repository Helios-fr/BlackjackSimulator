from utils import Card, Deck, Player
from simple_bot import Bot
import matplotlib.pyplot as plt

# Initialize game components
deck = Deck(1)
dealer = Player()
player = Player()
bot = Bot()
bot.capital = 1000

def reset_hands():
    player.clear_hand()
    dealer.clear_hand()

def simulate_round(bot):
    global deck
    if len(deck) < 20:
        deck = Deck(1)
    
    bet = bot.bet(deck)
    player.add(deck.draw(2))
    dealer.add(deck.draw(2))
    
    while player.get_hand_value() < 21:
        action = bot.turn(player, dealer.hand[0])
        if action == "Hit":
            player.add(deck.draw())
        else:
            break
    
    while dealer.get_hand_value() < 17:
        dealer.add(deck.draw())
    
    player_value = player.get_hand_value()
    dealer_value = dealer.get_hand_value()
    
    if player_value > 21:
        result = "Dealer" if dealer_value <= 21 else "Tie"
    elif dealer_value > 21 or player_value > dealer_value:
        result = "Player"
    elif player_value < dealer_value:
        result = "Dealer"
    else:
        result = "Tie"
    
    if result == "Player":
        bot.capital += bet
    elif result == "Dealer":
        bot.capital -= bet
    
    reset_hands()
    return result

def simulate(bot, rounds_to_simulate):
    capital_changes = []
    player_wins = dealer_wins = ties = 0

    for _ in range(rounds_to_simulate):
        if bot.capital <= 0:
            break
        capital_changes.append(bot.capital)
        result = simulate_round(bot)
        if result == "Player":
            player_wins += 1
        elif result == "Dealer":
            dealer_wins += 1
        else:
            ties += 1

    return capital_changes, player_wins, dealer_wins, ties

# Run simulation
capital_changes, player_wins, dealer_wins, ties = simulate(bot, 1000000)

# Plot results
plt.plot(capital_changes)
plt.show()

# Print results
print(f"Player wins: {player_wins}")
print(f"Dealer wins: {dealer_wins}")
print(f"Ties: {ties}")
print(f"Rounds: {len(capital_changes)}")
