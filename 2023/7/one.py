#part one: 

file = open('example.txt','r')
content = file.read()
# put race and distance in dictionary
def parse_data(data):
    hands = {}
    lines = content.split('\n')
    for hand in lines: 
        cards, bid = hand.split()
        hands[cards] = bid
    return hands

# get numbers of cards per hand
def calculations(hand):
    card_values = {'A':0, 'K': 0, 'Q': 0, 'J': 0, 'T': 0, '9': 0, '8': 0, '7': 0, '6': 0, '5': 0, '4': 0, '3': 0, '2': 0}
    for card in hand:
        count = hand.count(card)
        card_values[card] = count
        hand.replace(card, '') 
    for k,v in list(card_values.items()):
        if v == 0:
            del card_values[k]
    return card_values

def hand_strength(card_nums):
    strength = 0
    if 5 in card_nums.values():
        strength = 6
    if 4 in card_nums.values():
        strength = 6
    if 3 in card_nums.values() and 2 in card_nums.values():
        strength = 4
    if 3 in card_nums.values():
        strength = 3
    if 2 in card_nums.values():
        count = 0
        for num in card_nums.values():
            if num == 2:
                count += 1
        if count == 2:
            strength = 2
        else:
            strength = 1
    return strength

def convert_hand(hand):
    converted_hand = ''
    for card in hand:
        if card.isdigit():
            converted_hand += card + ' '
        elif card == 'T':
            converted_hand += '10 '
        elif card == 'J':
            converted_hand += '11 '
        elif card == 'Q':
            converted_hand += '13 '
        elif card == 'K':
            converted_hand += '14 '
        elif card == 'A':
            converted_hand += '15 '
    return converted_hand

# def compare_cards():

def compare_hands(data):
    ordered_hands = []
    for k, hands in data.items():
        for strength in range(1,6):
            if k == strength and len(hands) == 1:
                ordered_hands.append(hands)
            elif k == strength and len(hands) > 1:
                order_per_strength = []
                for hand in hands:
                    print(hand)
                    p = 0
                    for k,v in hand.items():
                        print(k)
                        cards = k.split()
                        for card in cards:
                            if int(card) > p:
                                p = int(card)
                            else:
                                order_per_strength.append(hands) 
                ordered_hands.append(order_per_strength)            
    return ordered_hands

# run the functions
def run(content):
    data = {6:[], 5:[], 4:[], 3:[], 2:[], 1:[]}
    hands = parse_data(content)
    for hand, bid in hands.items():
        card_nums = calculations(hand)
        strength = hand_strength(card_nums)
        hand = convert_hand(hand)
        combine_hand = {}
        combine_hand[hand] = bid
        data[strength].append(combine_hand)
    ordered_hands = compare_hands(data)
    #print(ordered_hands)
run(content)

file.close()