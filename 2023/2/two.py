# Part one: add all the possible games if there were 12 red, 13 green and 14 blue cubes
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
    split_info = line.split(':')
    cube_reveals = split_info[1].split(';')
    # loop through the groups of cubes
    for cubes in cube_reveals:
        split_cubes = cubes.split(',')
        for color in split_cubes:
            # for each color check if it's the highest
            if 'red' in color:
                get_num = color.split(' ')
                if int(get_num[1]) > red:
                    red = int(get_num[1])
            if 'green' in color:
                get_num = color.split(' ')
                if int(get_num[1]) > green:
                    green = int(get_num[1])              
            if 'blue' in color:
                get_num = color.split(' ')
                if int(get_num[1]) > blue:
                    blue = int(get_num[1])
    # multiple the number of cubes together, add to total
    power = red * blue * green
    total += power
print(total)
file.close()