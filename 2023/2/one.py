# Part one: add all the possible games if there were 12 red, 13 green and 14 blue cubes
file = open('input.txt','r')
content = file.readlines()

#placeholder for sum
total = 0
for line in content: 
    # boolean for valid game
    possible = True
    # split the line to relevant info
    get_id,games = line.split(': ')
    empty,game_id = get_id.split(' ')
    cube_reveals = games.split('; ')
    # loop through the groups of cubes
    for cubes in cube_reveals:
        split_cubes = cubes.split(', ')      
        for group in split_cubes:
            number,color = group.split(' ')
            # for each color check its not over the limit
            if 'red' in group and int(number) > 12:
                possible = False
            if 'green' in group and int(number) > 13:
                possible = False               
            if 'blue' in group and int(number) > 14:
                possible = False 
    # if the game is possible add the IDs up
    if possible:
        total += int(game_id) 
print(total)
file.close()