# Part one: using the input file, pull the first and last numbers from each line to make single number, then add each line to get total
# Part two: include spelled numbers

file = open('input.txt','r')
content = file.readlines()

# crack pot way of allowing overlapping numbers
# need to find better solution but for now works
def update_string(string):
    if "three" in string:
        string = string.replace("hre", "3")
    if "four" in string:
        string = string.replace("our", "4")
    if "five" in string:
        string = string.replace("iv", "5")
    if "seven" in string:
        string = string.replace("eve", "7")
    if "eight" in string:
        string = string.replace("igh", "8")
    if "nine" in string:
        string = string.replace("in", "9")
    if "one" in string:
        string = string.replace("ne", "1")
    if "two" in string:
        string = string.replace("two", "2")
    if "six" in string:
        string = string.replace("six", "6")
    return(string) 

# placeholder for total per line
total = []
#for each line, replace the spelled numbers
for line in content:
    number = ''
    line = update_string(line)
    # for each char add to placeholder per line
    for char in line:
        if char.isdigit():
            number += char
    # reduce down to first and last numbers
    if len(number) > 2:
        number = number[0] + number[len(number)-1]
    if len(number) == 1:
        number = number + number
    # convert strings to int
    total.append(int(number))
# add total and print
calibrationNum = sum(total) 
print(calibrationNum)    

file.close()