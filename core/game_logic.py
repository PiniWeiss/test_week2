from core.deck import CARDS_RANK
from core.player_io import ask_player_action

def calculate_hand_value(hand: list[dict]) -> int:
    hand_value = 0
    for i in range(len(hand)):
        for r in CARDS_RANK:
            if hand[i]["rank"] == r:
                hand_value += CARDS_RANK[r]
    return hand_value



def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:
    player["hand"] = [deck.pop(), deck.pop()]
    dealer["hand"] = [deck.pop(), deck.pop()]
    print(f"The player's hand: {calculate_hand_value(player["hand"])}")
    print(f"The dealer's hand: {calculate_hand_value(dealer["hand"])}")



def dealer_play(deck: list[dict], dealer: dict) -> bool:
    while calculate_hand_value(dealer["hand"]) < 17:
        dealer["hand"].append(deck.pop())
    if calculate_hand_value(dealer["hand"]) > 21:
        print("Dealer's lost!")
        return False
    else:
        return True



def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
    deal_two_each(deck, player, dealer)
    # print(f"The player hand size are: {calculate_hand_value(player["hand"])}")
    # print(f"The dealer hand size are: {calculate_hand_value(dealer["hand"])}")
    while calculate_hand_value(player["hand"]) <= 21:
        player_decision = ask_player_action()
        if player_decision == "H":
            player["hand"].append(deck.pop())
            print(f"Your hand size are: {calculate_hand_value(player["hand"])}")
            if calculate_hand_value(player["hand"]) > 21:
                print("You lost, maybe next time...")
                print(f"Your hand size are: {calculate_hand_value(player["hand"])}")
                break
        else:
            dealer_game =  dealer_play(deck, dealer)
            if dealer_game:
                player_hand = calculate_hand_value(player["hand"])
                dealer_hand = calculate_hand_value(dealer["hand"])
                if player_hand > dealer_hand:
                    print("Playrr won!!")
                    print(f"Player hand: {player_hand}")
                    print(f"Dealer hand: {dealer_hand}")
                    break
                elif dealer_hand > player_hand:
                    print("Dealer won!")
                    print(f"Player hand: {player_hand}")
                    print(f"Dealer hand: {dealer_hand}")
                    break
                else:
                    print("draw..") 
                    break
            else:
                print("player won!!")
                print(f"Your hand size are: {calculate_hand_value(player["hand"])}")
                print(f"The dealer hand size are: {calculate_hand_value(player["hand"])}")
                break
                
                    

            

            
        

