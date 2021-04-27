import io
import sys
import json
from collections import Counter

def get_top_leaderboard():
	f = io.open('leaderboard.json', mode='r', encoding='utf-8')

	try:
		number_of_players_to_print = int(sys.argv[2])
	except ValueError:
		raise ValueError("Second optional argument (number of players to print) must be an integer")
	except IndexError:
		number_of_players_to_print = 10

	if number_of_players_to_print <= 0:
		raise ValueError("Number of players to print must be more than 0")

	## ARGUMENT VALIDATION ##
	try:
		user_id = sys.argv[1]
	except IndexError:
		raise ValueError("User id must be provided as an argument. Try running \"python leaderboard {user_id} [{number_of_players_to_print}]\"")

	file_content = f.read()
	player_scores = json.loads(file_content)

	if user_id not in player_scores:
		raise ValueError("Current user id does not exist! Please specify an existing user id!")
	## END ARGUMENT VALIDATION ##

	selected_player = player_scores[user_id]

	sorted_players_by_bananas = get_sorted_players_list(player_scores)

	top_ten_players = sorted_players_by_bananas[:number_of_players_to_print]

	player_scores = [player['bananas'] for player in sorted_players_by_bananas]

	selected_player_rank = get_rank(selected_player['bananas'], player_scores)

	players_to_print = top_ten_players.copy()

	## if selected player ranking is higher than the number of players to print (default 10).
	if selected_player_rank > number_of_players_to_print:
		players_to_print[number_of_players_to_print - 1] = selected_player

	print ("{:<35} {:<15} {:<20} {:<15}".format('Name','Rank','Number of bananas','isCurrentUser?'))

	for player in players_to_print:

		player_name = player['name']
		if player['uid'] == selected_player['uid']:
			player_name = f"### {player['name']} ###"

		print ("{:<35} {:<15} {:<20} {}".format(player_name, get_rank(player['bananas'], player_scores), player['bananas'], player['subscribed']))


def get_sorted_players_list(leaderboard: dict):

	player_scores_list = [player_score for player_score in leaderboard.values()]
	player_scores_list.sort(key=lambda x: x['bananas'], reverse=True)

	return player_scores_list

def get_rank(score: int, scores: list):
	return scores.index(score) + 1

if __name__ == '__main__':
	get_top_leaderboard()