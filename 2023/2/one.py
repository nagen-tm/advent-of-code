# Part one: add all the possible games if there were 12 red, 13 green and 14 blue cubes
file = open('input.txt','r')
content = file.readlines()

#placeholder for sum
total = 0
for line in content: 
    # boolean for valid game
    possible = True
    # split the line to relevant info
    split_info = line.split(':')
    get_id = split_info[0].split(' ')
    cube_reveals = split_info[1].split(';')
    # loop through the groups of cubes
    for cubes in cube_reveals:
        split_cubes = cubes.split(',')
        for color in split_cubes:
            # for each color check its not over the limit
            if 'red' in color:
                get_num = color.split(' ')
                if int(get_num[1]) > 12:
                    possible = False
            if 'green' in color:
                get_num = color.split(' ')
                if int(get_num[1]) > 13:
                    possible = False               
            if 'blue' in color:
                get_num = color.split(' ')
                if int(get_num[1]) > 14:
                    possible = False 
    # if the game is possible add the IDs up
    if possible:
        total += int(get_id[1]) 
print(total)
file.close()