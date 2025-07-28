import random

cards = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']

def get_card_value(card):
    '''' to get the card value'''
    if card in ['Jack', 'Queen', 'King']:
        return 10
    elif card == 'Ace':
        return 11
    return card

def randomCard():
    '''shuffle the card'''
    return get_card_value(random.choice(cards))

def draw_hand():
    '''player's card'''
    card1 = randomCard()
    card2 = randomCard()
    return [card1, card2]

def calculate(hand):
    '''calculate the total cards'''
    total = 0
    aces = 0
    for card in hand:
        if card == 'Ace':
            aces += 1
            total += 11
        else: 
            total += get_card_value(card)
    while total > 21 and aces > 0:
        total -=10
        aces -=1
    return total


def play_again():
    ''' to start over or exit'''
    return input('Start again? y to continue or press any to exit.') == 'y'

my_hand, computer_hand = draw_hand(), draw_hand()
playing = True

while playing:
    print('\n')
    print(f'My card {my_hand} total: {calculate(my_hand)}')
    print(f"computer's first card [{computer_hand[0]}]")

    if calculate(my_hand) > 21:
        print('\n')
        print('computer wins!')
        player_total, computer_total = calculate(my_hand), calculate(computer_hand)
        print(f"your card {my_hand} = {calculate(my_hand)} TOTAL")
        print(f"computer's card {computer_hand} = {calculate(computer_hand)} TOTAL")
        if not play_again():
            print('Thankyou for playing!')
            break
        else: my_hand, computer_hand = draw_hand(), draw_hand()
        continue

    print('\n')
    add_pass = input('y to get another card or press any to pass: ')

    if add_pass == 'y':
        my_hand.append(randomCard())
    else:
        player_total, computer_total = calculate(my_hand), calculate(computer_hand)
        print(f"your card {my_hand} = {calculate(my_hand)} TOTAL")
        print(f"computer's card {computer_hand} = {calculate(computer_hand)} TOTAL")
        if player_total <= 21 and (player_total > computer_total or computer_total > 21):
            print('you win!')
        else:
            print('computer wins!')
        if not play_again():
            print('Thankyou for playing!')
            break
        my_hand, computer_hand = draw_hand(), draw_hand()
    








