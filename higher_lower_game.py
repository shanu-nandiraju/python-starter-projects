import random
import higher_lower_game_art
import higher_lower_game_data

current_score = 0
wrong = False

def data_presenter(the_winner):
    global current_score
    global wrong
    data_a = the_winner
    data_b = random.choice(higher_lower_game_data.data)
    while data_b == data_a:
        data_b = random.choice(higher_lower_game_data.data)
    print(f"Compare A: {data_a['name']}, a {data_a['description']}, from {data_a['country']}.")
    print(higher_lower_game_art.vs)
    print(f"Against B: {data_b['name']}, a {data_b['description']}, from {data_b['country']}.")
    answer = input("Who has more followers? Type 'A' or 'B': ").upper()
    if data_a['follower_count'] > data_b['follower_count']:
        if answer == 'A':
            current_score += 1
            print("\n" * 100)
            print(higher_lower_game_art.logo)
            print(f"You're right! Current score: {current_score}.")
            return data_a
    elif data_a['follower_count'] < data_b['follower_count']:
        if answer == 'B':
            current_score += 1
            print("\n" * 100)
            print(higher_lower_game_art.logo)
            print(f"You're right! Current score: {current_score}.")
            return data_b
    else:
        wrong = True
        return None

print(higher_lower_game_art.logo)
winner = random.choice(higher_lower_game_data.data)
while not wrong:
    winner = data_presenter(winner)
    if winner is None:
        break

print(f"Sorry, that's wrong. Final score: {current_score}")
