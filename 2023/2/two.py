# Part two: find the least amount of each color possible, multiply those together and find sum of each line
file = open('input.txt','r')
content = file.readlines()

#placeholder for sum
total = 0
for line in content: 
    # placeholder for lowest possible per color
    red = 0
    blue = 0
    green = 0
    # split the line to relevant info
    get_id,games = line.split(': ')
    cube_reveals = games.split('; ')
    # loop through the groups of cubes
    for cubes in cube_reveals:
        split_cubes = cubes.split(', ')
        for group in split_cubes:
            number,color = group.split(' ')
            # for each color check if it's the highest
            if 'red' in group and int(number) > red:
                red = int(number)
            if 'green' in group and int(number) > green:
                green = int(number)              
            if 'blue' in group and int(number) > blue:
                blue = int(number)
    # multiple the number of cubes together, add to total
    power = red * blue * green
    total += power
print(total)
file.close()