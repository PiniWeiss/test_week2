from core.deck import build_standard_deck, shuffle_by_suit
from core.game_logic import run_full_game


if __name__ == "__main__":
    deck_game = shuffle_by_suit(build_standard_deck())
    dealer, player = {"hand":None}, {"hand":None}
    run_full_game(deck_game,player,dealer)
