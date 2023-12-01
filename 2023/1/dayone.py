# Part one: using the input file, pull the first and last numbers from each line to make single number, then add each line to get total
# Part two: include spelled numbers

file = open('input.txt','r')
content = file.readlines()
# placeholder for total per line
total = []
num_dict = {'1':'one', '2': 'two', '3':'three','4':'four', '5':'five', '6':'six', '7':'seven' , '8':'eight', '9':'nine'}
# check by character for string numbers
for line in content:
    value = ''
    # enumerate lets you use the index of each character in the line
    for i, char in enumerate(line):
        if char.isdigit():
            value += char
        for num in num_dict:
            if line[i:].startswith(num_dict.get(num)):
                value += num
    # reduce down to first and last numbers
    if len(value) > 2:
        value = value[0] + value[len(value)-1]
    # if only one value, double it
    if len(value) == 1:
        value = value + value
    # convert strings to int
    total.append(int(value))
# add total and print
calibrationNum = sum(total) 
print(calibrationNum)    

file.close()