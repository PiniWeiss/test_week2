def ask_player_action() -> str:
    decision = input("Please enter your decision, H/S: ")
    if decision == "H":
        return decision
    elif decision == "S":
        return decision
    else:
        return ask_player_action()
    