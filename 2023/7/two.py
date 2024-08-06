#part one: 

file = open('example.txt','r')
content = file.read()
# put race and distance in dictionary
def parse_data(data):
    lines = content.split('\n')
    return lines

def eval(line):
    hand, bid = line.split()
    hand = hand.translate(str.maketrans('TJQKA', face))
    best = max(type(hand.replace('0', r)) for r in hand)
    return best, hand, int(bid)

def type(hand):
    return sorted(map(hand.count, hand), reverse=True)

for face in 'ABCDE', 'A0CDE':
    print(sum(rank * bid for rank, (*_, bid) in
        enumerate(sorted(map(eval, open('example.txt'))), start=1)))

# run the functions
def run(content):
    lines = parse_data(content)
    for hand in lines:
       data = eval(hand)
run(content)

file.close()