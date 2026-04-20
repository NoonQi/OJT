#Rock Paper Scissor
#https://replit.com/@techandnoon/boilerplate-rock-paper-scissors
def player(prev_play, opponent_history=[], play_order={}):
    # Reset state for each new opponent
    if not prev_play:
        opponent_history.clear()
        play_order.clear()
        return "R"

    opponent_history.append(prev_play)

    # Using n=3 or n=4 is ideal for these specific bots
    n = 3
    guess = "R"

    if len(opponent_history) > n:
        # Update the frequency map of sequences
        pattern = "".join(opponent_history[-(n+1):-1])
        full_seq = pattern + prev_play
        play_order[full_seq] = play_order.get(full_seq, 0) + 1

        # Predict based on the very last sequence seen
        last_n = "".join(opponent_history[-n:])
        potential_moves = ["R", "P", "S"]

        # Calculate which move the opponent is most likely to make
        sub_predictions = {
            move: play_order.get(last_n + move, 0) 
            for move in potential_moves
        }

        # Standardize max selection to avoid any argument errors
        prediction = max(potential_moves, key=lambda k: sub_predictions[k])

        # Counter the prediction
        ideal_response = {"R": "P", "P": "S", "S": "R"}
        guess = ideal_response[prediction]

    return guess

#o/p
#Final results: {'p1': 995, 'p2': 2, 'tie': 3}
#Player 1 win rate: 99.79939819458376%
#Final results: {'p1': 455, 'p2': 291, 'tie': 254}
#Player 1 win rate: 60.991957104557635%
#Final results: {'p1': 810, 'p2': 109, 'tie': 81}
#Player 1 win rate: 88.13928182807399%
#Final results: {'p1': 841, 'p2': 153, 'tie': 6}
#Final results: {'p1': 995, 'p2': 2, 'tie': 3}
#Player 1 win rate: 99.79939819458376%
#Final results: {'p1': 455, 'p2': 291, 'tie': 254}
#Player 1 win rate: 60.991957104557635%
#Final results: {'p1': 810, 'p2': 109, 'tie': 81}
#Player 1 win rate: 88.13928182807399%
#Final results: {'p1': 841, 'p2': 153, 'tie': 6}
#Player 1 win rate: 84.6076458752515%
