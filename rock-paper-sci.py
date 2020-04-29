#rock paper scissors

import random
rock_c = 0
paper_c = 0
scissor_c = 0

play_game = str(input("Do you want to play rock, paper, scissors?: "))
while play_game = 'y'
	choices = ['rock', 'paper', 'scissors']
	player_choice = input("rock, paper or scissors": )
	comp_choice = random.choice(choices)
	
	if player_choice == 'rock':
		if comp_choice == 'rock':
			print("It's a draw! - both rock")
		elif comp_choice == 'paper':
			print("You lose", comp_choice, player_choice)
		else:
			print("You win", comp_choice, player_choice)
		rock_c = rock_c + 1

	if player_choice == 'paper':
		if comp_choice == 'paper':
			print("It's a draw! - both paper")
		elif comp_choice == 'rock':
			print("You win", comp_choice, player_choice)
		else:
			print("You lose", comp_choice, player_choice)
		paper_c = paper_c + 1
	
	if player_choice == 'scissors'
		if comp_choice == 'scissors':	
			print("It's a draw! - both scissors")
		elif comp_choice == 'paper':
			print("You win", comp_choice, player_choice)
		else:
			print("You lose", comp_choice, player_choice)	
		scissor_c = scissor_c + 1

count = rock_c + paper_c + scissor_c
avg(r) = rock_c / count
avg(p) = paper_c / count
avg(s) = scissor_c / count

if avg(r) > (avg(p) and avg(s))
	comp_choice = 'paper'
if avg(p) > (avg(s) and avg(r))
	comp_choice = 'scissors'
if avg(s) > (avg(r) and avg(p))
	comp_choice = 'rock'