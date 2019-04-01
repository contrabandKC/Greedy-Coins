
################################
################################
## Author        : Erik Marquez
## Due           : 9.1.2018
## Class         : comp sci 101 -002 TuTh 5:30-6:45
## program number:2. Greedy Coins
##
##  Two player coin game, played by flipping 3 coins
##      first player to reach 20 wins
##
## Step 1. Prompt user to enter name
## Step 2. Play greedy coins by flipping three coins. 
## Step 3. ask player if he wants to play again
################################


import random
def user_action():
    """User decides to flip or hold"""
    choice = True
    while choice == True:
        user = input(' (F)lip Again or (H)old?').lower()
        if user == 'f':
            choice = False
        elif  user == 'h':
            choice = False
        else:
            choice = True
    return user

###
### Calling all the veriables
###

coin1 = ()
coin2 = ()
coin3 = ()

player_score = 0
ai_score = 0
pot = 0
ai_pot = 0

player_win = True
ai_win = False


user = ('f')

play = 'Y'

##
## Intro to game
##

print('WELCOME TO GREEDY DICE!!\n')

user_name = input('What is your name\n')


##
##Game Loop 
##

while play != 'no'and play != 'n':


    print('SCORE %s : 0 AI : 0 \n' % user_name)

## 
##Round loop
##
    
    while ai_score <= 20:

        if player_score >= 20:
            break
        
        user = ('f')

        if player_win == True:
            play = input('Your turn. Hit enter to continue.\n')

    ###
    ###User Loop Check to see if you need user of player_win
    ###
        while user == 'f':

            if player_score >= 20:  
                break
            
            if ai_score >= 20:
                break

            if player_win == False:
                break

            play=()
            user=()
            
 ## Coins User
            
            coin_one = random.randint(0,1)
            coin_two = random.randint(0,1)
            coin_three = random.randint(0,1)
            coins = coin_one + coin_two + coin_three
            pot += coin_one + coin_two + coin_three
            
            if coin_one == 1:
                coin1 = 'H'
            else:
                coin1 = 'T'
            if coin_two == 1:
                coin2 = 'H'   
            else:
                coin2 = 'T'
            if coin_three == 1:
                coin3 = 'H'
            else:
                coin3 = 'T'
##
##Conditional statments on the round, pot, or user winning
##
            if coins == 0:
                user = 'f'
                pot = 0
                print('\ncoins : ',coin1,coin2,coin3,'Pot  : ',pot, end = '  ')
                print('BUST \n \n')
                break

            print('Coins : ',coin1,coin2,coin3,'Pot  : ',pot,end='  ')

            if pot >= 20:
                player_score += pot
                break

            user = user_action()
          
        if user == 'h':
            player_score += pot
            pot = 0
            user = 'f'
            print('\n \nSCORE %s : %d    AI : %d \n' % (user_name, player_score, ai_score))

        
        if player_score < 20:
            play = input('It’s the computers turn. Hit enter to continue.\n')


            
    ###
    ### ai_loop
    ###
        while ai_pot < 8:                                 

            if player_score >= 20:  
                break
            
            if ai_score >= 20:
                break
            if ai_pot >= 10:
                break

            
            player_win = True
    
            
            coin_one = random.randint(0,1)
            coin_two = random.randint(0,1)
            coin_three = random.randint(0,1)
            ai_coins = coin_one + coin_two + coin_three
            ai_pot += coin_one + coin_two + coin_three

            if coin_one == 1:
                coin1 = 'H'
            else:
                coin1 = 'T'
            if coin_two == 1:
                coin2 = 'H'   
            else:
                coin2 = 'T'
            if coin_three == 1:
                coin3 = 'H'
            else:
                coin3 = 'T'
##
##Conditional statments for AI on the round, pot, or user winning
##
            if ai_coins == 0:
                ai_pot =  0
                print('\nAI coins : ',coin1,coin2,coin3,'Pot  : ',ai_pot, end ='  ')
                print('BUST')
                break

            print('Coins : ',coin1,coin2,coin3,'Pot  : ',ai_pot,)

        ai_score += ai_pot

        ai_pot = 0

        if player_score <= 20:  
            print('\n \nSCORE %s : %d     AI : %d \n' % (user_name, player_score, ai_score))


    ##
    ## Winners statments
    ##

    if player_score >=20:
        player_win = False
        ai_win = True
        print('%s you are the Winner!! \n' % user_name)

    if ai_score >= 20:
        player_win = True
        ai_win = False
        print('Ai is the Winner\n')

##
## Replay
##
        
    player_score= 0
    ai_score= 0
    play = ()

    
    while play != 'n':
        if play == 'no':
            break
        if play == 'y':
            break
        if play == "yes":
            break
    
        play=input('Do you want to play Greedy Coin again? (YES/Y/NO/N)\n')
        play=play.lower()

print('Thank You for playing!')

