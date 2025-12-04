def ask_player_action() -> str:
    decision = input("Please enter your decision, H/S: ")
    if decision == "H":
        return decision
    elif decision == "S":
        return decision
    else:
        print("The only options to choose from are H or S.\n")
        return ask_player_action()
    