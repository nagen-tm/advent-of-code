# all function returns True or False
# zip function pairs 

def check_safety(line):
    data = [int(n) for n in line.split()]
    ascending = all(a < b for a, b in zip(data, data[1:]))
    decending = all(a > b for a, b in zip(data, data[1:]))
    diffference = all(abs(a - b) <= 3 for a, b in zip(data, data[1:]))
    return ascending, decending, diffference

def read_file(filename):
    with open(filename) as file:
        content = file.readlines()
        count = 0
        for line in content:
            ascending, decending, diffference = check_safety(line)
            if (ascending or decending) and diffference:
                count += 1
            else:
                data = line.split()
                check = False
                for i in range(len(data)):
                    ascending, decending, diffference = check_safety(' '.join(data[:i] + data[i + 1:]))
                    if (ascending or decending) and diffference and not check:
                        check = True
                if check:
                    count +=1
    return count

print("Example: ", read_file("2024/2/example.txt"))
print("Input: ", read_file("2024/2/input.txt"))
