from random import randint

CARDS_SUITE = ["H", "D", "S", "C"]
CARDS_RANK = {"A":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":10,"Q":10,"K":10}


def build_standard_deck() -> list[dict]:
    deck_list = []
    for s in CARDS_SUITE:
        for r in CARDS_RANK:
            deck_list.append({"rank":r, "suit":s}) 
    return deck_list


def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:
    while swaps > 0:
        i = randint(0,51)
        j = randint(0,51)
        if deck[i] == deck[j]:
            continue
        if deck[i]["suit"] == "H" and j%5 != 0:
            continue
        if deck[i]["suit"] == "C" and j%3 != 0:
            continue
        if deck[i]["suit"] == "D" and j%2 != 0:
            continue
        if deck[i]["suit"] == "S" and j%7 != 0:
            continue
        deck[i], deck[j] = deck[j], deck[i]
        swaps -= 1
    return deck
