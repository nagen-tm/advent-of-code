#part two: 

file = open('input.txt','r')
content = file.readlines()
total = 0
extra_cards = {}
line_num = 1
# create the dictionary with game number, counting first singular card
for line in content:
    extra_cards[line_num] = 1
    line_num += 1

for line in content:
    # placeholder for winning numbers per line
    count = []
    # split the info needed
    card, winners = line.strip().split('| ')
    winning_nums = winners.split()
    card_num, nums = card.split(': ')
    empty, game = card_num.split()
    your_numbers = nums.split()
    # remove the empty spaces from single digit numbers
    while("" in your_numbers):
        your_numbers.remove("")
    while("" in winning_nums):
        winning_nums.remove("")
    # find the winning numbers you have per card
    for number in your_numbers:
        if number in winning_nums:
            count.append(number) 
    # get current number of cards
    number_of_copies =  extra_cards[int(game)]
    # based off the number of winning numbers add to the dictionary based on game number
    for card in range(1, len(count)+1):
        extra_cards[int(game)+card] += number_of_copies

print(sum(extra_cards.values()))

file.close()