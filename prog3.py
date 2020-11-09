#Grading ID: D3998
#CIS 443-01
#Program 3
#Due Date: Monday November 2, 2020 11:59pm
#This program stimulates a game of craps

import random
games_play=1000000
list_of_wins= {}
list_of_losses= {}


def roll_dice():
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    return (die1, die2)  # pack die face values into a tuple

def display_dice(dice):
    """Display one roll of the two dice."""
    die1, die2 = dice  # unpack the tuple into variables die1 and die2
    print(f'Player rolled {die1} + {die2} = {sum(dice)}')
   
def game():
    roll = 1
    die_values = roll_dice()  # first roll
    #display_dice(die_values)
    # determine game status and point, based on first roll
    sum_of_dice = sum(die_values)
    if sum_of_dice in (7, 11):  # win
        game_status = 'WON'
    elif sum_of_dice in (2, 3, 12):  # lose
        game_status = 'LOST'
    else:  # remember point
        game_status = 'CONTINUE'
        my_point = sum_of_dice
    # continue rolling until player wins or loses
    while game_status == 'CONTINUE':
        die_values = roll_dice()
        roll +=1
        #display_dice(die_values)
        sum_of_dice = sum(die_values)
    
        if sum_of_dice == my_point:  # win by making point
            game_status = 'WON'
        elif sum_of_dice == 7:  # lose by rolling 7
            game_status = 'LOST'
    # display "wins" or "loses" message
    if game_status == 'WON':
        if roll in list_of_wins:
                list_of_wins[roll] += 1 
        else:
            list_of_wins[roll] = 1 
    else:
        if roll in list_of_losses:
            list_of_losses[roll] += 1 
        else:
            list_of_losses[roll] = 1


for x in range(games_play):
    game()
# print("Wins")  
# print(list_of_wins)
# print("Losses")
# print(list_of_losses)  
    

total_wins=sum(list_of_wins.values())/games_play
print(f'Percentage of wins {total_wins:.2%}')
total_losses=sum(list_of_losses.values())/games_play
print(f'Percentage of losses {total_losses:.2%}')

max_roll= 200

cum_resolved = 0
print('Percentage of wins/losses based on total number of rolls')
print('{:>25}{:>30} '.format('% Resolved', 'Cumulative %'))
print('{:<5}{:>22} {:>30}'.format('Rolls', 'on this roll','of games resolved'))
for i in range(1,max_roll+1):
    if i in list_of_wins or i in list_of_losses:
        resolved = 0
        if i in list_of_wins:
            resolved += list_of_wins[i]
        if i in list_of_losses:
            resolved+= list_of_losses[i]
        cum_resolved+=resolved
        print("{:<5} {:>20} {:>25}".format(i, resolved/games_play,cum_resolved/games_play))
      
        


