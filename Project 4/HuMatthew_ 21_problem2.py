#importing random
import random

#finding the random numbers for both the player and dealer
dealer_cards = [random.randint(1, 11), random.randint(1, 11)]
player_cards = [random.randint(1, 11), random.randint(1, 11)]
winner = None

print("Let's Play 21...")

#creating a loop which ends after the user is done inputting or the game ends
while True:
    dealer_score = sum(dealer_cards)
    player_score = sum(player_cards)

    print(f"Dealer's cards: {dealer_cards[0]} X")
    print(f"Your cards: {' '.join(map(str, player_cards))}")


    hitstay = input("Would you like to hit or stay? ")


#creating a condition where if the user says hit then it will hit and generates who won
    if hitstay == 'Hit'or hitstay == 'hit':
        new_card = random.randint(1, 11)
        player_cards.append(new_card)
        print(f"You drew a {new_card}")
        if sum(player_cards) > 21:
            print("You bust! Dealer wins!")
            winner = "Dealer"
            break

        #creatinga  condition where if the user says stay then it will stay and until the user says hit or the game ends 
    elif hitstay == 'Stay'or hitstay == 'stay':
        while sum(dealer_cards) < 17:
            new_card = random.randint(1, 11)
            dealer_cards.append(new_card)
            print(f"Dealer drew a {new_card}")
            if sum(dealer_cards) > 21:
                print("Dealer busts! You win!")
                winner = "Player"
                break
        #saying who won under specific condtions
        if not winner:
            if sum(dealer_cards) > sum(player_cards):
                print("Dealer wins!")
                winner = "Dealer"
            elif sum(player_cards) > sum(dealer_cards):
                print("You win!")
                winner = "Player"
            else:
                print("Tie game!")
                winner = "Tie"
        break

#saying who won the game 
print(f"Final score -- Dealer: {sum(dealer_cards)}, You: {sum(player_cards)}")
print(f"{winner} wins!")
