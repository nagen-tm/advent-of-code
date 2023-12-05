#part one: find the points from winning scratch off tickets 

file = open('input.txt','r')
content = file.readlines()
points = 0
for line in content:
    # placeholder for winning numbers per line
    count = []
    # split the info needed
    card, winners = line.strip().split('| ')
    winning_nums = winners.split(' ')
    card_num, nums = card.split(': ')
    your_numbers = nums.split(' ')
    # remove the empty spaces from single digit numbers
    while("" in your_numbers):
        your_numbers.remove("")
    while("" in winning_nums):
        winning_nums.remove("")
    # find the winning numbers you have per card
    for number in your_numbers:
        if number in winning_nums:
            count.append(number) 
    # add up the points
    if len(count) == 1:
        points += 1
    elif len(count) > 1:
        points += 2**(len(count)-1) 
    
print(points)

file.close()